# C API

This page explains how to install the **C version** of HPR-LP.

---

## 1. Prerequisites

- **NVIDIA GPU** with CUDA support  
- **CUDA Toolkit** (≥ 12.4 recommended)  
- **CUDA libraries**: cuBLAS, cuSOLVER, cuSPARSE (included with CUDA Toolkit)  

Quick checks:
```bash
nvidia-smi
nvcc --version
```

---

## 2. Clone the Repository

```bash
git clone https://github.com/PolyU-IOR/HPR-LP-C.git
cd HPR-LP-C
```

Or download and extract the ZIP file from GitHub.

---

## 3. Build

From the project root:
```bash
make clean       # Remove build artifacts
make             # Build everything (recommended)
```

This creates:
- `lib/libhprlp.a` — Static library for C/C++ linking  
- `lib/libhprlp.so` — Shared library for language bindings (Python/Julia/MATLAB)  
- `build/solve_mps_file` — MPS solver executable

---

## Next Steps

- See the [Interfaces](../Interfaces/C%20interfaces/index.md) section for C usage.