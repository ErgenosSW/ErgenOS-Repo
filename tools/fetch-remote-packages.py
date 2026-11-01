#!/usr/bin/env python3
"""Fetch large signed packages that are published as GitHub Release assets."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "remote-packages.json"
ALLOWED_URL = "https://github.com/ErgenosSW/ErgenProton-WoW/releases/download/"
SHA256 = re.compile(r"[0-9a-f]{64}")


def fetch(url: str, destination: Path, expected_size: int, expected_hash: str) -> None:
    if not url.startswith(ALLOWED_URL):
        raise SystemExit(f"Untrusted package URL: {url}")
    if destination.name != Path(url).name or not SHA256.fullmatch(expected_hash):
        raise SystemExit(f"Invalid manifest entry: {destination.name}")

    if destination.is_file() and destination.stat().st_size == expected_size:
        digest = hashlib.sha256()
        with destination.open("rb") as existing:
            while chunk := existing.read(1024 * 1024):
                digest.update(chunk)
        if digest.hexdigest() == expected_hash:
            print(f"Already verified {destination.name}")
            return

    temporary = destination.with_name(destination.name + ".part")
    digest = hashlib.sha256()
    size = 0
    request = urllib.request.Request(url, headers={"User-Agent": "ErgenOS-Repo/1"})
    try:
        with urllib.request.urlopen(request) as response, temporary.open("wb") as output:
            while chunk := response.read(1024 * 1024):
                output.write(chunk)
                digest.update(chunk)
                size += len(chunk)
        if size != expected_size:
            raise SystemExit(f"Unexpected size for {destination.name}: {size}")
        if digest.hexdigest() != expected_hash:
            raise SystemExit(f"SHA-256 mismatch for {destination.name}")
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", type=Path, default=ROOT / "x86_64")
    arguments = parser.parse_args()
    payload = json.loads(MANIFEST.read_text())
    if payload.get("schema_version") != 1 or not isinstance(payload.get("packages"), list):
        raise SystemExit("Unsupported remote package manifest")
    arguments.destination.mkdir(parents=True, exist_ok=True)
    for package in payload["packages"]:
        fetch(
            package["url"],
            arguments.destination / package["filename"],
            package["size"],
            package["sha256"],
        )
        fetch(
            package["signature_url"],
            arguments.destination / package["signature"],
            package["signature_size"],
            package["signature_sha256"],
        )
        print(f"Fetched and verified {package['filename']}")


if __name__ == "__main__":
    main()
