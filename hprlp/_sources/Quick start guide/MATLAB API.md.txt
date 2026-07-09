# MATLAB API

This page explains how to install the **MATLAB version** of HPR-LP.

## 1. Prerequisites

Before using HPR-LP, make sure the following dependencies are installed:

- **MATLAB** (Recommended version: `R2020a` or later)
- **C++ Compiler** (Required for MEX compilation; e.g., GCC on Linux/macOS, MSVC on Windows)

---


## 2. Download the Repository


Download and extract the ZIP file from [HPR-LP-MATLAB](https://github.com/PolyU-IOR/HPR-LP-MATLAB).

---


## 3. Install Dependencies

To set up the HPR-LP environment, run the setup script in MATLAB:
```matlab
cd /path/to/HPR-LP/matlab
setup_hprlp  % Compiles MEX reader and configures paths
```

## Next Steps

- See the [Interfaces](../Interfaces/MATLAB%20interfaces.md) section for Python usage.

