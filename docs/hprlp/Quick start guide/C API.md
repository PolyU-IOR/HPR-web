# C API

HPR-LP-C is the GPU-accelerated C/CUDA implementation of HPR-LP. The commands
below follow the official [HPR-LP-C repository](https://github.com/PolyU-IOR/HPR-LP-C).

## Prerequisites

- Linux on x86-64.
- An NVIDIA GPU supported by the selected CUDA Toolkit.
- The NVIDIA CUDA Toolkit, including `nvcc`, cuBLAS, cuSOLVER, cuSPARSE, and
  the CUDA driver development library.
- GCC/G++ with C++17 support, supported by the selected CUDA Toolkit
  (GCC 9–12 recommended).
- GNU Make or CMake 3.18 or newer.
- zlib development headers.

On Ubuntu 22.04:

```bash
sudo apt-get update
sudo apt-get install -y build-essential cmake zlib1g-dev
```

Install the CUDA Toolkit separately using NVIDIA's instructions. If CUDA is
not installed at `/usr/local/cuda`, set `CUDA_PATH` or `CUDA_HOME`.

## Clone, build, and run

```bash
git clone https://github.com/PolyU-IOR/HPR-LP-C.git
cd HPR-LP-C
make clean && make -j
./build/solve_mps_file -i data/model.mps --tol 1e-6 --time-limit 1000
```

The build creates `build/solve_mps_file`, `lib/libhprlp.a`, and `lib/libhprlp.so`.
Replace `data/model.mps` with your own `.mps` or `.mps.gz` file when needed.

For the latest published source archive:

```bash
unzip HPR-LP-C-0.1.3.zip
cd HPR-LP-C-0.1.3
make clean && make -j
./build/solve_mps_file -i data/model.mps --tol 1e-6 --time-limit 1000
```

Download the archive from [C Releases](../Releases/C%20Releases.md).

## GPU architecture selection

The Makefile detects the first visible GPU through `nvidia-smi`.

| GPU family | Compute capability | Build architecture |
|---|---:|---:|
| NVIDIA B200 | 10.0 | `sm_100` |
| NVIDIA H100 | 9.0 | `sm_90` |
| NVIDIA A100 | 8.0 | `sm_80` |
| GeForce RTX 30 series | 8.6 | `sm_86` |
| GeForce RTX 40 series | 8.9 | `sm_89` |
| GeForce RTX 50 series | 12.0 | `sm_120` |

The selected CUDA Toolkit must support the detected architecture. If no GPU is
visible, `nvcc` chooses its supported default. Run `make help` to inspect the
selection; `GPU_SM=<arch>` remains available for cross-builds.

CUDA 13.3 and newer use the experimental `cusparseSpMVOp` API; older toolkits
use `cusparseSpMV`. Selection happens at compile time from the toolkit headers.

## CMake build and installation

```bash
CUDA_PATH="${CUDA_PATH:-/usr/local/cuda}"
cmake -S . -B build-cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CUDA_COMPILER="$CUDA_PATH/bin/nvcc"
cmake --build build-cmake
cmake --install build-cmake --prefix "$HOME/.local"
```

This also detects the first visible GPU automatically. For an explicit H100
cross-build, use a separate directory and set compute capability 9.0:

```bash
CUDA_PATH="${CUDA_PATH:-/usr/local/cuda}"
cmake -S . -B build-h100 \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CUDA_COMPILER="$CUDA_PATH/bin/nvcc" \
  -DCMAKE_CUDA_ARCHITECTURES=90
cmake --build build-h100
```

An explicit `CMAKE_CUDA_ARCHITECTURES` value overrides automatic detection.
Make and CMake build the vendored GPU-Presolver-C backend by default. Use
`-DBUILD_GPU_PRESOLVER=OFF` for a smaller PSLP-only CMake build.

For a Make-based installation:

```bash
make clean && make -j
make install PREFIX="$HOME/.local"
export PATH="$HOME/.local/bin:$PATH"
export LD_LIBRARY_PATH="$HOME/.local/lib:${LD_LIBRARY_PATH:-}"
```

## Next steps

- [C Version: usage, options, and language interfaces](../Interfaces/C%20interfaces/index.md)
- [C releases and source downloads](../Releases/C%20Releases.md)
- [Official troubleshooting instructions](https://github.com/PolyU-IOR/HPR-LP-C#troubleshooting)
