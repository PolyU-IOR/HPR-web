# Julia Releases

Release notes and downloads from the official [HPR-LP releases](https://github.com/PolyU-IOR/HPR-LP/releases), checked on **12 November 2026**.

The latest published release is **v0.1.7**. The ZIP and tar.gz links below are source archives. Install the Julia dependencies using the [Julia quick start](../Quick%20start%20guide/Julia%20API.md).

## v0.1.7

**Published:** 22 May 2026.

Fixes primal solution recovery, adds Curtis–Reid scaling, and falls back to solving the original model when the presolver fails.

[Release notes](https://github.com/PolyU-IOR/HPR-LP/releases/tag/v0.1.7) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.7.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.7.tar.gz)

## v0.1.6

**Published:** 7 May 2026.

Adds PSLP presolve (`params.presolve = "PSLP"`) and GPU presolve (`params.presolve = "GPU"`), developed by @ljw2024polyu and collaborators.

[Release notes](https://github.com/PolyU-IOR/HPR-LP/releases/tag/v0.1.6) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.6.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.6.tar.gz)

## v0.1.5

**Published:** 5 April 2026.

Optimizes GPU kernels and workflows for an approximately 10% per-iteration speedup.

[Release notes](https://github.com/PolyU-IOR/HPR-LP/releases/tag/v0.1.5) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.5.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.5.tar.gz)

## v0.1.4

**Published:** 20 March 2026.

Improves GPU efficiency with CUDA Graph updates, stabilizes and optimizes power-iteration eigenvalue estimation, adds MOI/JuMP optimizer integration (`demo/demo_JuMP.jl`), and supports warm starts through `initial_x` and `initial_y`.

[Release notes](https://github.com/PolyU-IOR/HPR-LP/releases/tag/v0.1.4) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.4.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.4.tar.gz)

## v0.1.3

**Published:** 17 October 2025.

Refines parameter adjustment for greater stability and relative KKT/duality gap accuracy up to **1e-9**, and improves JuMP modeling integration. On an NVIDIA A100-SXM4-80GB, the Mittelmann benchmark without presolve solved **47 / 49** instances at 1e-4 tolerance and **41 / 49** at 1e-9, with a 3,600 s time limit.

[Release notes](https://github.com/PolyU-IOR/HPR-LP/releases/tag/v0.1.3) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.3.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.3.tar.gz)

## v0.1.2

**Published:** 28 September 2025.

Rewrites SpMV with preprocessing and preallocated buffers, and refactors CUDA kernels to reduce memory traffic and improve occupancy. At 1e-8 accuracy, the release notes report an 11% SGM10 improvement on the Mittelmann LP set and 7% on large MIPLIB 2017 LP relaxations compared with v0.1.1.

[Release notes](https://github.com/PolyU-IOR/HPR-LP/releases/tag/v0.1.2) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.2.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.2.tar.gz)

Additional release download: [HPR-LP_v012_bug_fixed.zip](https://github.com/PolyU-IOR/HPR-LP/releases/download/v0.1.2/HPR-LP_v012_bug_fixed.zip).

## v0.1.1

**Published:** 9 September 2025.

Updates model reformulation, adaptive restarts and penalty tuning; rewrites or fuses CUDA kernels; and removes `sigma` and `sigma_fixed` from the public parameters. At 1e-8 accuracy, the notes report improvements of 14% on Mittelmann and 95% on large MIPLIB 2017 LP relaxations compared with v0.1.0.

[Release notes](https://github.com/PolyU-IOR/HPR-LP/releases/tag/v0.1.1) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.1.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.1.tar.gz)

## v0.1.0

**Published:** 9 September 2025.

The initial GPU-accelerated Julia implementation of the Halpern–Peaceman–Rachford method for linear programming. The release notes describe the preliminary release dated 4 July 2025.

[Release notes](https://github.com/PolyU-IOR/HPR-LP/releases/tag/v0.1.0) · [Source code (ZIP)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.0.zip) · [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.0.tar.gz)
