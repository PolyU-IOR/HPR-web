# Julia API

This page explains how to install the **Julia version** of HPR-QP.

---

## 1. Prerequisites

- **Julia** ≥ 1.10.4  
- **CUDA**: NVIDIA GPU with proper CUDA driver  
- **System tools**: Standard C/C++ toolchain (for dependencies)

Check that CUDA is available in Julia:
```julia
using CUDA
CUDA.versioninfo()
```

---

## 2. Pick the Right Solver and Clone the Repository
If you need to solve a LASSO problem (with an $l_1$ regularizer) or a QAP instance where the matrix form of $Q$ is unavailable, please refer to the HPR-QP_QAP_LASSO module.
```bash
git clone https://github.com/PolyU-IOR/HPRQLP.git
cd HPR-QP_QAP_LASSO
```

otherwise, for convex QP (COP) problems where the matrix form of $Q$ is available, please refer to the HPR-QP module.
```bash
git clone https://github.com/PolyU-IOR/HPRQLP.git
cd HPR-QP
```

Or download and extract the ZIP file from GitHub.

---

## 3. Install Dependencies

Inside the project root, run:
```bash
julia --project -e 'using Pkg; Pkg.instantiate()'
```

This will install all required Julia dependencies (including CUDA.jl).



---

## Next Steps

- See the [Interfaces](../Interfaces/index.md) section for Julia usage.
