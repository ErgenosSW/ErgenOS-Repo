## 2026-10-25 - Package refresh

- ErgenCTL 1.1.0.dev-12, source revision 158f0058307ce813d538266af5f5958d4b567f7d.
- ErgenPac 1.0.1-2, source revision 89eb66b6a66a7c824dedf921ef10fd2b73d541a9,
  includes responsive navigation changes after v1.0.1.
- Add previously unpublished ergenos-theme 1.2.0-3, from ErgenOS-Linux
  revision 2524693461058553b7e91add31dd3cf19fb7240f.
- Source checksums passed; 126 ErgenCTL and 44 ErgenPac tests passed.
- Built on the maintainer host with makepkg --nodeps; no dependency installation
  or target-system update test was performed. This is not a clean-chroot build.
- All database entries were checked against package SHA-256 sums and signatures;
  both repository database signatures were verified with the published key.
- Existing package archives remain available. Welcome and Secure Boot are unchanged.

# Changelog

## ErgenPac 1.0.1-1 — 2026-10-11

Publish the Gaming catalog refresh fix and fakeroot dependency. Package and both
repository databases were signed and verified; the owner performed publication.

## ErgenPac 1.0.0-1 — 2026-10-11

Publish the optional gaming launcher/tool catalog, with signed package and databases.

## Application redesign baseline

ErgenCTL 1.1.0.dev-9, Welcome 1.0.3-1 and ErgenPac 0.2.4-1 introduced the redesigned
application interfaces. ErgenPac is superseded by 1.0.1-1 in the current database.
Older package files may remain available for recovery.

## Theme package status

The 1.2.0-2 theme used by the ISO is currently a local build package. Public ISO
hosting and checksums are available in the ErgenOS 1.2 release; publishing the
theme in this package repository remains a separate step.
