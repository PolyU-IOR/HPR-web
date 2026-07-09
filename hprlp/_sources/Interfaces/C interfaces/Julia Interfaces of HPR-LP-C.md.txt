# Julia Binding of HPR-LP-C
This page provides quick-start examples for using the Julia interfaces of HPR-LP-C to build and solve linear programs directly from matrices or MPS files.

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
**`Model(A, AL, AU, l, u, c)`**
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
---

See the [github](https://github.com/PolyU-IOR/HPR-LP-C/tree/main/bindings/julia) for more details.
