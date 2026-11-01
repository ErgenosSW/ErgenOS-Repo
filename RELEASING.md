# Maintaining the signed Pacman repository

This repository distributes packages through GitHub Pages; it does not need a
GitHub Release for every database change. Application tags and GitHub Releases
belong in their respective source repositories. The optional Hyprland preview
is separate from the GNOME package set and is not added automatically.

Build and test packages from recorded source revisions. Increment pkgrel when
shipping different content under the same pkgver. Keep previous package archives
for recovery, sign each new package locally with key
28F9539131BC392DAF4099C595FE7988F432AFDA, and update both databases with:

```sh
repo-add --sign --key 28F9539131BC392DAF4099C595FE7988F432AFDA --include-sigs \
  x86_64/ergenos.db.tar.zst x86_64/NEW-PACKAGE.pkg.tar.zst
python3 tools/fetch-remote-packages.py
python3 tools/validate-repository.py
```

Packages larger than GitHub's per-file Git limit are uploaded with their detached
signature to the application's GitHub Release. Record the immutable URLs, sizes
and SHA-256 values in `remote-packages.json`, add the signed package to the
database with `repo-add --include-sigs`, then remove the package archive and its
signature from the Git working tree. The Pages workflow downloads and validates
the recorded assets before deployment.

Do not disable required signature checking. Review files and commit/push manually.
After Pages deployment, download the public db and files aliases with their
signatures and run the same integrity checks against the published artifacts.
A local validation does not prove that a deployment has completed.
