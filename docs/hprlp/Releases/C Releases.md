# C Releases

Release notes and downloads from the official [HPR-LP-C releases](https://github.com/PolyU-IOR/HPR-LP-C/releases), checked on **12 November 2026**.

The latest published release is **v0.1.3**. The ZIP and tar.gz links below are source archives. Build or instantiate the source using the [C quick start](../Quick%20start%20guide/C%20API.md).

## v0.1.3

**Published:** 14 September 2026.

Introduces structure-aware SpMV kernels, GPU-Presolver-C integration with optional folding, and sparsity-aware updates. On the **49-instance Hans benchmark**, it solves **49 / 49** instances and reduces SGM10 total time from **12.74 s to 5.93 s** compared with v0.1.2, a **2.15× speedup**.

[Release notes](https://github.com/PolyU-IOR/HPR-LP-C/releases/tag/v0.1.3) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP-C/archive/refs/tags/v0.1.3.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP-C/archive/refs/tags/v0.1.3.tar.gz)

## v0.1.2

**Published:** 9 May 2026.

Adds customized sparse SpMV GPU kernels, reduces GPU/CPU synchronization overhead, supports PSLP presolve, and adds Curtis–Reid scaling.

[Release notes](https://github.com/PolyU-IOR/HPR-LP-C/releases/tag/v0.1.2) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP-C/archive/refs/tags/v0.1.2.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP-C/archive/refs/tags/v0.1.2.tar.gz)

## v0.1.1

**Published:** 3 February 2026.

Adds CUDA Graphs and aligns the Power Iteration implementation. See [pull request #4](https://github.com/PolyU-IOR/HPR-LP-C/pull/4) for the upstream change.

[Release notes](https://github.com/PolyU-IOR/HPR-LP-C/releases/tag/v0.1.1) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP-C/archive/refs/tags/v0.1.1.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP-C/archive/refs/tags/v0.1.1.tar.gz)

## v0.1.0

**Published:** 4 January 2026.

The first public release of the C/CUDA implementation of HPR-LP.

[Release notes](https://github.com/PolyU-IOR/HPR-LP-C/releases/tag/v0.1.0) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP-C/archive/refs/tags/v0.1.0.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP-C/archive/refs/tags/v0.1.0.tar.gz)
