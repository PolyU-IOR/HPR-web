# MATLAB Binding of HPR-LP-C
This page provides quick-start examples for using the MATLAB interfaces of HPR-LP-C to build and solve linear programs directly from matrices or MPS files.


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
## Example 2: Solve from MPS File

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

### `hprlp.Parameters`
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

---

See the [github](https://github.com/PolyU-IOR/HPR-LP-C/tree/main/bindings/matlab) for more details.