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

## ErgenOS 1.2 package status

- ErgenPac 1.0.1-1: optional Gaming catalog and automatic isolated catalog refresh.
- ErgenCTL 1.1.0.dev-9: redesigned UI, hybrid graphics diagnostics and update verification.
- ErgenOS Welcome 1.0.3-1: redesigned portal and language-aware project resources.
- Optional ErgenOS Secure Boot 0.2.0.dev-6: existing signed-boot recovery backend.

The validated 1.2 ISO uses ergenos-theme 1.2.0-2 from a separate local build
repository. That theme is not yet published here. The public ErgenOS 1.2 ISO is
available from the [ErgenOS 1.2 release](https://github.com/ErgenosSW/ErgenOS-Linux/releases/tag/v1.2.0), independently of package publication in this repository. See [CHANGELOG.md](CHANGELOG.md).

## Current first-party packages

- ErgenCTL
- ErgenOS Secure Boot
- ErgenOS Welcome
- ErgenPac
- ErgenOS keyring
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
