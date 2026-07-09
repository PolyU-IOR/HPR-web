# Julia API

This page explains how to install the **Julia version** of HPR-LP.

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

## 2. Clone the Repository

```bash
git clone https://github.com/PolyU-IOR/HPR-LP.git
cd HPR-LP
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

## 4. Verify Installation

Start Julia in project mode:
```bash
julia --project
```

and test whether the environment loads without errors:
```julia
using HPRLP
```

If no error appears, the installation is successful.

---

## Next Steps

- See the [Interfaces](../Interfaces/Julia%20interfaces.md) section for Julia usage.
