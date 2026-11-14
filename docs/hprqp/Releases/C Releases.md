# C Releases

Release notes and downloads from the official [HPR-QP-C releases](https://github.com/PolyU-IOR/HPR-QP-C/releases), checked on **12 November 2026**.

The latest published release is **v0.1.1**. The downloads are source archives to build on the target host. Follow the [C quick start](../Quick%20start%20guide/C%20API.md).

## v0.1.1

**Published:** 30 October 2026.

Enables native C++ CPU polishing and conservative automatic equality Gram
scaling by default. A certified CPU point can terminate a solve with
`polished_optimal`; intermediate CPU points do not feed back into GPU iterations.

Adds GPU second-order-cone support, a sparse-factor convex QCQP-to-SOC interface,
and support for diagonal convex `QCMATRIX` constraints in MPS input. Unsupported
quadratic input is explicitly rejected. Supported CUDA 13.3+ builds use SpMVOp
automatically, with guarded packed/fused sparse GPU access and documented fallbacks.

Improves the plain Make build with verified local dependency setup, matching CUDA
runtime libraries, and CUDA-driver startup checks. Plain `make` no longer
requires CMake. The release is source code to build on the target host; native
polishing uses BLAS/LAPACK and OpenSSL `libcrypto`, and Python 3 is used for build
helpers. Recompile C/C++ clients against the matching headers and libraries and
use a fresh dataset output directory after upgrading.

The attached `HPR-QP-C-v0.1.1.zip` contains tracked source files from the release
commit. `SHA256SUMS` verifies that ZIP. This release tags the existing public
commit and makes no new performance benchmark claim.

[Release notes](https://github.com/PolyU-IOR/HPR-QP-C/releases/tag/v0.1.1) · [HPR-QP-C-v0.1.1.zip](https://github.com/PolyU-IOR/HPR-QP-C/releases/download/v0.1.1/HPR-QP-C-v0.1.1.zip) · [SHA256SUMS](https://github.com/PolyU-IOR/HPR-QP-C/releases/download/v0.1.1/SHA256SUMS) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-QP-C/archive/refs/tags/v0.1.1.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-QP-C/archive/refs/tags/v0.1.1.tar.gz)

## v0.1.0

**Published:** 9 May 2026.

The first public release of the HPR-QP C implementation supports both GPU
and CPU solving and roughly aligns with Julia HPR-QP v0.1.1.

[Release notes](https://github.com/PolyU-IOR/HPR-QP-C/releases/tag/v0.1.0) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-QP-C/archive/refs/tags/v0.1.0.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-QP-C/archive/refs/tags/v0.1.0.tar.gz)
