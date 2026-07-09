# Python API
<!-- Coming soon... -->
This page explains how to install the **Python version** of HPR-LP.

---


## 1. Prerequisites

- **CUDA Toolkit** (≥ 12.4 recommended)  

Build a new environment by conda and activate it.

```bash
conda create -n hprlp_python python=3.12
conda activate hprlp_python
```

Quick checks:
```bash
python --version
nvidia-smi
```

---


## 2. Clone the Repository

```bash
git clone https://github.com/PolyU-IOR/HPR-LP-Python.git
cd HPR-LP-Python
```

Or download and extract the ZIP file from GitHub.

---


## 3. Install Dependencies

Install PyTorch **first** (choose the right CUDA wheel for your system):
```bash
pip install torch torchvision
```

Then install the remaining packages:
```bash
pip install -r requirements.txt
```

## Next Steps

- See the [Interfaces](../Interfaces/Python%20interfaces.md) section for Python usage.