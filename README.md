<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# pkg-rpm-tinycompress

RPM packaging for
[tinycompress](https://github.com/alsa-project/tinycompress) on
CentOS Stream 10 (aarch64).

tinycompress is a user-space library for the ALSA compressed audio
interface. It enables offloaded audio decoding using the kernel compress
interface (e.g., MP3, AAC offload on Qualcomm platforms), providing a
minimal API for compressed audio offload. The package is maintained on the
CentOS Stream 10 (`c10s`) branch and uses the shared GitHub Actions build
and release workflow.

## CI Workflows

| Workflow | Trigger | Purpose |
|---|---|---|
| [`build-on-pr.yml`](.github/workflows/build-on-pr.yml) | Pull request | Build the RPM(s) so reviewers confirm the package still builds. Read-only — never publishes. |
| [`pkg-release.yml`](.github/workflows/pkg-release.yml) | Manual (`workflow_dispatch`) | Build **and** publish the RPM(s) to Artifactory, behind an approval gate. |

The GitHub Actions workflows use the shared
[`qcom-rpm-utils`](https://github.com/qualcomm-linux/qcom-rpm-utils) build
environment and run `rpmbuild` inside the prebuilt `rpm-builder` container
image for the runner's host architecture.

---

## Repository Layout

The `c10s` branch contains the RPM packaging files:

| File | Purpose |
|---|---|
| `tinycompress.spec` | Builds the tinycompress runtime library and `-devel` subpackage. |
| `sources` | SHA-512 checksum for the upstream source archive. |
| `README.md` | Package and repository documentation. |
| `LICENSE.txt` | License for the RPM packaging repository. |

The source archive is not committed to this repository. The spec file's
`Source0` points to the upstream release, and the checksum in `sources` is
verified before the RPM is built.

---

## Packages

- `tinycompress`: tinycompress runtime shared library.
- `tinycompress-devel`: Headers and pkg-config files for building
  applications that use the tinycompress library.

---

## Updating the package version

This is the everyday workflow — **two edits on `c10s`, no tarball in git**:

1. Bump `Version:` in the spec (and the `Source0:` URL if its path changed).
2. Recompute the checksum for the new tarball:
   ```bash
   sha512sum --tag tinycompress-<newversion>.tar.gz > sources
   ```
3. Commit the spec + `sources`, open a PR (build verifies it), merge, then run
   **Release**. The first release fetches the new upstream tarball, verifies it,
   and caches it back to Artifactory automatically.

## License

This project is licensed under the BSD 3-Clause License. See [LICENSE.txt](LICENSE.txt) for the complete license text.

The upstream tinycompress library is licensed separately under
`BSD-3-Clause AND LGPL-2.1-only`, as declared by `tinycompress.spec`.
