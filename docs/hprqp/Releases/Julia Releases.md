# Julia Releases

Release notes and downloads from the official [HPR-QP releases](https://github.com/PolyU-IOR/HPR-QP/releases), checked on **12 November 2026**.

The latest published release is **v0.1.1**. The downloads are source archives. Install the Julia dependencies using the [Julia quick start](../Quick%20start%20guide/Julia%20API.md).

## v0.1.1

**Published:** 30 December 2025.

Unifies standard QP, QAP, and LASSO in one codebase through a modular Q
operator system. Adds a full CPU implementation alongside GPU acceleration,
with device selection through `use_gpu`, and native JuMP/MathOptInterface
integration.

Warm starts use `initial_x` and `initial_y`. The `auto_save=true` option saves
the best solution during optimization so long-running solves can resume from
previously saved states.

[Release notes](https://github.com/PolyU-IOR/HPR-QP/releases/tag/v0.1.1) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-QP/archive/refs/tags/v0.1.1.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-QP/archive/refs/tags/v0.1.1.tar.gz)

## v0.1.0

**Published:** 11 September 2025.

The preliminary Julia release provides a GPU-accelerated solver for convex
composite quadratic programming using the Halpern Peaceman–Rachford method.
The upstream release notes identify the preliminary release as **7 July 2025**;
GitHub's publication date is shown above.

[Release notes](https://github.com/PolyU-IOR/HPR-QP/releases/tag/v0.1.0) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-QP/archive/refs/tags/v0.1.0.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-QP/archive/refs/tags/v0.1.0.tar.gz)
