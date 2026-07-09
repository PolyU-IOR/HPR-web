# Python Binding of HPR-LP-C
This page provides quick-start examples for using the Python interfaces of HPR-LP-C to build and solve linear programs directly from matrices or MPS files.


---

## Test problem (LP)

The default demo problem we ship is a small linear program of the form


$$
\begin{aligned}
\min \quad & - 3 x_1 - 5 x_2\\
\text{s.t.} \quad & x_1 + 2 x_2 \le 10, \\
& 3 x_1 + x_2 \le 12, \\
& x_1 \ge 0, \\
& x_2 \ge 0.
\end{aligned}
$$

---

## Example 1: Build model directly from matrices

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




### `Model.from_arrays(A, AL, AU, l, u, c)`
Create an LP model from matrices and vectors.

**Arguments:**
- `A` - Constraint matrix (scipy sparse or dense)
- `AL`, `AU` - Constraint bounds (numpy arrays)
- `l`, `u` - Variable bounds (numpy arrays)
- `c` - Objective coefficients (numpy array)

**Returns:** Model object

---

## Example 2: Solve from MPS File

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

## `Model.from_mps(filename)`
Create an LP model from the MPS file.

**Arguments:**
- `filename` - Path to MPS file

**Returns:** Model object

### `Model.solve(param=None)`
Solve the LP model.

**Arguments:**
- `param` - (Optional) Parameters object

**Returns:** Results object

---
See the [github](https://github.com/PolyU-IOR/HPR-LP-C/tree/main/bindings/python) for more details.