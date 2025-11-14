# C interfaces

This page shows the **C interface** of HPR-LP with a minimal, task-oriented guide. Use the CLI to solve `.mps` files, or link your C/C++ program against `libhprlp` for programmatic access.

---

## Usage

### Solving from MPS Files
Use the prebuilt executable in `build/`. The default settings enable GPU, standard scalings, and a 3600-second time limit.

```bash
# Show help
./build/solve_mps_file -h

# Run with default settings
./build/solve_mps_file -i data/model.mps

# Run with custom settings
./build/solve_mps_file -i data/model.mps --tol 1e-4 --time-limit 3600
```

### Using as a Library
Link against `libhprlp.a` (static) or `libhprlp.so` (shared) and include the public headers under `include/`.  
See the `examples/` directory for small, self-contained demos (C and C++) showing compilation flags and basic API calls.

For more details, check `examples/c(cpp)/README.md` on integrating HPR-LP-C into external projects (include paths, link order, and CUDA libs).

---

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `-i, --input <path>` | Path to input MPS file | *required* |
| `--device <id>` | CUDA device ID | 0 |
| `--max-iter <N>` | Maximum iterations | unlimited |
| `--tol <eps>` | Stopping tolerance | 1e-4 |
| `--time-limit <sec>` | Time limit in seconds | 3600 |
| `--check-iter <N>` | Convergence check interval | 150 |
| `--ruiz <true/false>` | Ruiz scaling | true |
| `--pock <true/false>` | Pock-Chambolle scaling | true |
| `--bc <true/false>` | Bounds/cost scaling | true |
| `-h, --help` | Show help message | - |

> Tip: If the runtime can’t find `libhprlp.so`, set `LD_LIBRARY_PATH=$PWD/lib:$LD_LIBRARY_PATH` (or install to a system path).

---

## Language Interface Installation

**Python (pip only):**
```bash
cd HPR-LP-C/bindings/python
python -m pip install .         # or: python -m pip install -e .
```

**Julia Interface:**
```bash
cd bindings/julia
bash install.sh
```

**MATLAB Interface:**
```bash
cd bindings/matlab
bash install.sh
```

See the respective README files in `bindings/` for usage, version notes, and troubleshooting.

---

## Language Interfaces
HPR-LP-C provides native interfaces for multiple languages:

### **Python**:  pybind11 bindings (see the [github](https://github.com/PolyU-IOR/HPR-LP-C/tree/main/bindings/python) for more details)

#### Example 1: Build model directly from matrices

```bash
cd examples
python example_direct_lp.py              # Solve from arrays
```

**Quick overview**:
The following snippet demonstrates how to define and solve an LP problem directly from matrices.
For a complete version with additional options, see example_direct_lp.py.

```python
import numpy as np
from scipy import sparse
import hprlp

# Define LP: minimize c'x subject to AL <= Ax <= AU, l <= x <= u
A = sparse.csr_matrix([[1.0, 2.0], [3.0, 1.0]])
AL = np.array([-np.inf, -np.inf])
AU = np.array([10.0, 12.0])
l = np.array([0.0, 0.0])
u = np.array([np.inf, np.inf])
c = np.array([-3.0, -5.0])

# Create model
model = hprlp.Model.from_arrays(A, AL, AU, l, u, c)

# Configure solver
param = hprlp.Parameters()
param.stop_tol = 1e-9
param.device_number = 0

# Solve
result = model.solve(param)

if result.is_optimal():
    print(f"Optimal: {result.primal_obj}")
    print(f"Solution: {result.x}")
```




#### `Model.from_arrays(A, AL, AU, l, u, c)`
Create an LP model from matrices and vectors.

**Arguments:**
- `A` - Constraint matrix (scipy sparse or dense)
- `AL`, `AU` - Constraint bounds (numpy arrays)
- `l`, `u` - Variable bounds (numpy arrays)
- `c` - Objective coefficients (numpy array)

**Returns:** Model object

---

### Example 2: Solve from MPS File

```bash
cd examples
python example_mps_file     # Solve from MPS file
```

**Quick overview:**
The following snippet demonstrates how to define and solve an LP problem directly from an MPS file. For a complete version with additional options, see example_mps_file.py.

```python
import hprlp

# Create model from MPS file
model = hprlp.Model.from_mps("problem.mps")

# Solve
result = model.solve()
print(result)
```

### `Model.from_mps(filename)`
Create an LP model from the MPS file.

**Arguments:**
- `filename` - Path to MPS file

**Returns:** Model object

### `Model.solve(param=None)`
Solve the LP model.

**Arguments:**
- `param` - (Optional) Parameters object

**Returns:** Results object




### **MATLAB**: MEX interface with OOP wrapper (see the [github](https://github.com/PolyU-IOR/HPR-LP-C/tree/main/bindings/matlab) for more details)  

#### Example 1: Build model directly from matrices

```bash
cd examples
matlab -batch "example_direct_lp"              # Solve from arrays
```

Or run interactively in MATLAB:
```matlab
cd examples
example_direct_lp
```

**Quick overview**:
The following snippet demonstrates how to define and solve an LP problem directly from matrices.
For a complete version with additional options, see example_direct_lp.m.


```matlab
% Define LP: minimize c'x subject to AL <= Ax <= AU, l <= x <= u
A = sparse([1.0, 2.0; 3.0, 1.0]);
AL = [-inf; -inf];
AU = [10.0; 12.0];
l = [0.0; 0.0];
u = [inf; inf];
c = [-3.0; -5.0];

% Create model
model = hprlp.Model.from_arrays(A, AL, AU, l, u, c);

% Configure solver
param = hprlp.Parameters();
param.stop_tol = 1e-9;
param.device_number = 0;

% Solve
result = model.solve(param);

if strcmp(result.status, 'OPTIMAL')
    fprintf('Optimal: %.6f\n', result.primal_obj);
    fprintf('Solution: x = [%.6f, %.6f]\n', result.x(1), result.x(2));
end
```

### `hprlp.Model.from_arrays(A, AL, AU, l, u, c)`
Create an LP model from matrices and vectors.

**Arguments:**
- `A` - Constraint matrix (m×n sparse or dense)
- `AL`, `AU` - Constraint bounds (column vectors)
- `l`, `u` - Variable bounds (column vectors)
- `c` - Objective coefficients (column vector)

**Returns:** Model object

---
### Example 2: Solve from MPS File

```bash
cd examples
matlab -batch "example_mps_file"              # Solve from MPS file
```

Or run interactively in MATLAB:
```matlab
cd examples
example_mps_file
```

**Quick overview**:
The following snippet demonstrates how to define and solve an LP problem from an MPS file.
For a complete version with additional options, see example_mps_file.m.

```matlab
% Create model from MPS file
model = hprlp.Model.from_mps('problem.mps');

% Solve
result = model.solve();
disp(result);
```
### `hprlp.Model.from_mps(filename)`
Create an LP model from the MPS file.

**Arguments:**
- `filename` - Path to MPS file

**Returns:** Model object

### `model.solve(param)`
Solve the LP model.

**Arguments:**
- `param` - (Optional) Parameters object. If omitted, default parameters are used.

**Returns:** Result object

## `hprlp.Parameters`
Solver configuration:
- `max_iter` - Maximum iterations (default: 2147483647)
- `stop_tol` - Stopping tolerance (default: 1e-4)
- `time_limit` - Time limit in seconds (default: 3600)
- `device_number` - CUDA device ID (default: 0)
- `check_iter` - Convergence check interval (default: 150)
- `use_Ruiz_scaling` - Ruiz scaling (default: true)
- `use_Pock_Chambolle_scaling` - Pock-Chambolle scaling (default: true)
- `use_bc_scaling` - Bounds/cost scaling (default: true)

**Example:**
```matlab
param = hprlp.Parameters();
param.stop_tol = 1e-9;
param.device_number = 0;
```

### **Julia**: Native Julia wrapper (see the [github](https://github.com/PolyU-IOR/HPR-LP-C/tree/main/bindings/julia) for more details)  

### Example 1: Build model directly from matrices
```bash
cd examples
julia --project=../package example_direct_lp.jl
```

**Quick overview:**
The following snippet demonstrates how to define and solve a small LP problem directly from matrices.
For a complete version with additional options, see example_direct_lp.jl.
```julia
using HPRLP
using SparseArrays

# Define LP: minimize c'x subject to AL ≤ A*x ≤ AU, l ≤ x ≤ u
A  = sparse([1.0 2.0; 3.0 1.0])
AL = [-Inf, -Inf]
AU = [10.0, 12.0]
l  = [0.0, 0.0]
u  = [Inf, Inf]
c  = [-3.0, -5.0]

# Create model
model = Model(A, AL, AU, l, u, c)

# Configure solver parameters
params = Parameters(
    stop_tol = 1e-9,
    device_number = 0
)

# Solve
result = solve(model, params)

if is_optimal(result)
    println("Optimal objective: ", result.primal_obj)
    println("Optimal solution:  ", result.x)
end
```
---
### `Model(A, AL, AU, l, u, c)`
Create an LP model directly from matrices and vectors.

| Argument | Description |
|-----------|--------------|
| `A` | Sparse constraint matrix (m×n) |
| `AL`, `AU` | Constraint bounds |
| `l`, `u` | Variable bounds |
| `c` | Objective coefficients |

**Returns:** `Model` object

## Example 2: Read model from an MPS file

```
cd examples
julia --project=../package example_mps_file.jl
```

**Quick overview:**
The following snippet demonstrates how to define and solve an LP problem directly from an MPS file. For a complete version with additional options, see example_mps_file.jl.
```julia
using HPRLP

# Create model from MPS file
model = Model("problem.mps")

# Solve
result = solve(model)
println(result)
```

---

### `Model(filename::String)`
Create an LP model by reading an MPS file.

| Argument | Description |
|-----------|--------------|
| `filename` | Path to the MPS file |

**Returns:** `Model` object

---

### `solve(model::Model, params=nothing)`
Solve the given LP model.

| Argument | Description |
|-----------|--------------|
| `model` | LP model object |
| `params` | Optional solver parameters |
| **Returns** | `Results` object |

---


## Example 3: Use JuMP to construct and solve LPs

```
cd examples
julia --project=../package example_jump.jl
```


- **C/C++**: Direct API usage (see `examples/c/` and `examples/cpp/` for minimal build/run demos)

