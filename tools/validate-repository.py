#!/usr/bin/env python3
"""Verify repository databases, indexed package checksums and detached signatures."""
import base64
import hashlib
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
KEY = '28F9539131BC392DAF4099C595FE7988F432AFDA'

def run(*args):
    return subprocess.check_output(args, text=True, stderr=subprocess.STDOUT)

with tempfile.TemporaryDirectory(prefix='ergenos-repo-verify-') as home:
    gpg = ['gpg', '--batch', '--no-autostart', '--no-auto-key-retrieve', '--homedir', home]
    run(*gpg, '--import', str(ROOT / 'keys/ergenos.asc'))
    fingerprints = run(*gpg, '--with-colons', '--fingerprint')
    if f'fpr:::::::::{KEY}:' not in fingerprints:
        raise SystemExit('Unexpected repository signing key')
    def verify(path):
        output = run(*gpg, '--status-fd', '1', '--verify', str(path) + '.sig', str(path))
        if f'[GNUPG:] VALIDSIG {KEY} ' not in output:
            raise SystemExit(f'Wrong signer: {path}')
    directory = ROOT / 'x86_64'
    databases = [directory / f'ergenos.{kind}.tar.zst' for kind in ('db', 'files')]
    for database in databases:
        verify(database)
    def inventory(database):
        records = {}
        for member in run('bsdtar', '-tf', str(database)).splitlines():
            if not member.endswith('/desc'):
                continue
            fields = {}
            for block in run('bsdtar', '-xOf', str(database), member).strip().split('\n\n'):
                key, *values = block.splitlines()
                fields[key.strip('%')] = values
            name = fields['NAME'][0]
            if name in records:
                raise SystemExit(f'Duplicate database entry: {name}')
            records[name] = fields
        if not records:
            raise SystemExit(f'Empty repository: {database}')
        return records
    records = inventory(databases[0])
    files_records = inventory(databases[1])
    if records != files_records:
        raise SystemExit('db and files package metadata differ')
    for name, fields in sorted(records.items()):
        filename = fields['FILENAME'][0]
        if Path(filename).name != filename:
            raise SystemExit(f'Invalid package filename: {filename}')
        package = directory / filename
        if hashlib.sha256(package.read_bytes()).hexdigest() != fields['SHA256SUM'][0]:
            raise SystemExit(f'Checksum mismatch: {package}')
        verify(package)
        if fields.get('PGPSIG'):
            if base64.b64decode(fields['PGPSIG'][0], validate=True) != Path(str(package) + '.sig').read_bytes():
                raise SystemExit(f'Embedded package signature differs: {package}')
        print(name, fields['VERSION'][0])
    for package in sorted(directory.glob('*.pkg.tar.zst')):
        verify(package)
    for alias, target in [('ergenos.db', 'ergenos.db.tar.zst'), ('ergenos.files', 'ergenos.files.tar.zst'),
                          ('ergenos.db.sig', 'ergenos.db.tar.zst.sig'), ('ergenos.files.sig', 'ergenos.files.tar.zst.sig')]:
        if (directory / alias).read_bytes() != (directory / target).read_bytes():
            raise SystemExit(f'Pacman alias differs: {alias}')
    print(f'Validated {len(records)} indexed packages and all retained package signatures.')
