# C API

HPR-QP-C is the CUDA/C implementation of HPR-QP. The commands below follow the
official [HPR-QP-C repository](https://github.com/PolyU-IOR/HPR-QP-C).

## Prerequisites

- A C/C++ compiler, GNU Make, and Python 3 for build helpers.
- OpenSSL `libcrypto` (version 3 or 1.1).
- A compatible NVIDIA CUDA Toolkit and NVIDIA driver for GPU solving.
- BLAS/LAPACK for native CPU polishing. On Debian/Ubuntu Linux x86_64, Make can
  download missing libraries and their runtimes into the checkout's
  `.deps/native/` directory using verified APT metadata. This requires
  `apt-get`/`dpkg-deb`, usable package indexes, and network access. Other
  platforms must provide compatible BLAS/LAPACK libraries themselves.
- cuDSS for the default GPU build with equality Gram scaling. Make reuses a
  compatible installation or downloads the NVIDIA cuDSS **0.7.1.4** archive for
  CUDA 12 or 13, verifies its SHA256, and installs it into `.deps/cudss/`.
  Linux x86_64 and SBSA are supported; the initial download is about 110–120 MiB.

Plain `make` uses the C/C++ compilers directly and **does not require CMake**.
Dependency setup stays inside the checkout; it does not install or change the
CUDA driver or system packages. NumPy and SciPy are not runtime dependencies
of the native CPU polishing worker.

## Clone, build, and run on a GPU

```sh
git clone https://github.com/PolyU-IOR/HPR-QP-C.git
cd HPR-QP-C
make && \
./build-cuda/solve_qp model.mps --use-gpu 1 --device-number 0 --stoptol 1e-8 --time-limit 1000
```

Replace `model.mps` with your input file and `0` with the desired GPU index.
The `&&` runs the solver only after a successful build. Native CPU polishing,
conservative automatic equality Gram selection, and supported GPU optimizations
are enabled by default.

Alternatively, download a source archive from [C Releases](../Releases/C%20Releases.md),
extract it, and run the same `make && ...` command from the extracted source
directory. The v0.1.1 release includes an official source ZIP and a
`SHA256SUMS` file, as well as GitHub's generated source ZIP and tar.gz archives.

## CUDA and dependency configuration

When several CUDA toolkits are installed, use the same `CUDA_ROOT` when building
and checking cuDSS:

```sh
make CUDA_ROOT=/usr/local/cuda-13.3
make check-cudss CUDA_ROOT=/usr/local/cuda-13.3
```

The path is an example; select a toolkit compatible with your GPU and driver.
The build checks CUDA startup and records the chosen runtime in
`.deps/cuda-runtime.json`. Re-run `make` after moving to another host or changing
the CUDA/driver installation.

To reuse an existing cuDSS installation:

```sh
make CUDSS_ROOT=/path/to/cudss
```

That directory must contain `include/cudss.h` and its matching shared library.
To prepare dependencies separately:

```sh
make setup-native
make setup-cudss
```

`AUTO_INSTALL_NATIVE_DEPS=0` disables native dependency downloads;
`make AUTO_INSTALL_CUDSS=0` disables cuDSS downloads and fails if required cuDSS
is missing. For an older checkout previously built without cuDSS, run
`make gpu-clean` before rebuilding.

## CPU-only build

```sh
make cpu && \
./build/solve_qp model.mps --stoptol 1e-6 --time-limit 3600
```

CPU-only builds do not require cuDSS. See the
[official installation instructions](https://github.com/PolyU-IOR/HPR-QP-C#install)
for dependency details and supported fallbacks.

## Shared library and language wrappers

Install the shared library and associated runtime files:

```sh
make install
```

When copying a GPU build, keep `hprqp_polish_worker` and its `lib/` directory
(when present) beside `build-cuda/solve_qp`. `make install` places the worker
under `libexec/hprqp`.

- [C Version: complete installation, usage, and solver options](../Interfaces/C%20interfaces.md)
- [Julia wrapper for HPR-QP-C](../Interfaces/C%20interfaces/Julia%20Wrapper.md)
- [Python wrapper for HPR-QP-C](../Interfaces/C%20interfaces/Python%20Wrapper.md)
- [C releases and source downloads](../Releases/C%20Releases.md)
