# ErgenOS Package Repository

Official signed Pacman repository for ErgenOS applications and supporting
packages.

The repository is consumed automatically by ErgenOS. Packages and repository
databases are signed with the ErgenOS package-signing key.

## Repository configuration

ErgenOS systems use the following Pacman configuration:

```ini
[ergenos]
SigLevel = Required
Server = https://ergenossw.github.io/ErgenOS-Repo/$arch
```

Do not reduce `SigLevel` to bypass a signature error. Refresh the system
keyring and investigate the failed package or database instead.

## Signing key

The public key is available at [`keys/ergenos.asc`](keys/ergenos.asc).

```text
Fingerprint: 28F9 5391 31BC 392D AF40  99C5 95FE 7988 F432 AFDA
Identity: ErgenOS Package Signing
```

The `ergenos-keyring` package installs and trusts this key on ErgenOS. The
fingerprint should be verified before trusting the key on another Arch-based
system.

## ErgenOS 1.3 package status

- ErgenPac 1.0.1-3: optional Gaming catalog and Gaming Check integration.
- ErgenCTL 1.1.0.dev-13: diagnostics, recovery and Gaming Check.
- ErgenOS Welcome 1.0.3-1: redesigned portal and language-aware project resources.
- Optional ErgenOS Secure Boot 0.2.0.dev-6: existing signed-boot recovery backend.
- Optional ErgenProton-WoW 0.2.0-1: WoW-focused compatibility tool, not installed
  by default and not included in the ISO.

The repository includes ergenos-theme 1.2.0-3. ErgenCTL and ErgenPac are built
from pinned source revisions. See CHANGELOG.md for build and validation scope.

## Current first-party packages

- ErgenCTL
- ErgenOS Secure Boot
- ErgenOS Welcome
- ErgenPac
- ErgenOS keyring
- ErgenProton-WoW
- signed shim binaries used by ErgenOS Secure Boot

Older package versions may remain in `x86_64/` for rollback or recovery. The
signed repository database determines the version offered by Pacman.

## Project links

- [ErgenOS](https://github.com/ErgenosSW/ErgenOS-Linux)
- [Official website](https://ergenossw.github.io/ErgenOS-Website/)
- [Installation guide](https://ergenossw.github.io/ErgenOS-Website/installation.html)
- [Secure Boot guide](https://ergenossw.github.io/ErgenOS-Website/secure-boot.html)

This repository distributes both original ErgenOS software and third-party
components. Individual packages retain their respective licenses and upstream
attribution.

## Maintainer validation

Run the remote-package fetcher followed by the validator before publication:

```sh
python3 tools/fetch-remote-packages.py
python3 tools/validate-repository.py
```

The fetcher downloads large release assets from an allowlisted GitHub release
and checks their recorded size and SHA-256. The validator then verifies the
expected signing key, both signed databases, indexed package SHA-256 sums,
embedded signatures when present, all retained package signatures and Pacman
alias files. GitHub Actions performs the same checks before assembling the Pages
artifact, so large packages are served through the normal ErgenOS repository
without storing them in Git. See RELEASING.md.
