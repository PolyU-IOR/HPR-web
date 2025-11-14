# Julia Version

This page shows how to use the **Julia interface** of HPR-LP: run demos, build custom problems, adjust solver settings, and interpret results.

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

## Usage 1: Test Instances in MPS Format

### Setting Data and Result Paths
Before running the scripts, please modify `run_single_file.jl` or `run_dataset.jl` in the scripts directory to specify the data path and result path according to your setup.

### Running a Single Instance
To test the script on a single instance (`.mps` file):

```bash
julia --project scripts/run_single_file.jl
```

### Running All Instances in a Directory
To process all `.mps` files in a directory:

```bash
julia --project scripts/run_dataset.jl
```

## Usage 2: Define Your LP Model in Julia Scripts

### Example 1: Build and Export an LP Model Using JuMP

This example shows how to build an LP model in JuMP, export it to MPS format, and solve it with HPR-LP.

```bash
julia --project demo/demo_JuMP.jl
```

The script:

- Builds a linear programming (LP) model.  
- Saves the model as an MPS file.  
- Uses HPR-LP to solve the LP instance.  

> **Tip:** If the model may be infeasible or unbounded, you can use HiGHS to check it.

```julia
using JuMP, HiGHS
## read a model from file (or create in other ways)
mps_file_path = "xxx" # your file path
model = read_from_file(mps_file_path)
## set HiGHS as the optimizer
set_optimizer(model, HiGHS.Optimizer)
## solve it
optimize!(model)
```

### Example 2: Define an LP instance directly in Julia

This example shows how to construct and solve a linear programming problem directly in Julia without relying on JuMP.

```bash
julia --project demo/demo_Abc.jl
```

## Note on First-Time Execution Performance

The first run of an instance may feel slow because Julia compiles code on the first execution (JIT compilation).


```{tip}
**Tip for Better Performance:**  
To reduce repeated compilation overhead, it’s recommended to run scripts from an **IDE like VS Code** or the **Julia REPL** in the terminal.
```

**Start Julia REPL with the project environment**

```bash
julia --project
```

Then, at the Julia REPL, run `demo/demo_Abc.jl` (or other scripts):

```julia
include("demo/demo_Abc.jl")
```

```{admonition} CAUTION
If you encounter the error message:

`Error: Error during loading of extension AtomixCUDAExt of Atomix, use Base.retry_load_extensions() to retry`.

This is usually temporary. Wait a few moments and the extension will load automatically.
```

---

## Parameters

Below is a list of the parameters in HPR-LP along with their default values and usage:

```{list-table}
:header-rows: 1
:widths: 20 20 60

* - **Parameter**
  - **Default Value**
  - **Description**
* - `warm_up`
  - `false`
  - Determines if a warm-up phase is performed before main execution.
* - `time_limit`
  - `3600`
  - Maximum allowed runtime (seconds) for the algorithm.
* - `stoptol`
  - `1e-4`
  - Stopping tolerance for convergence checks.
* - `device_number`
  - `0`
  - GPU device number (only relevant if `use_gpu` is true).
* - `max_iter`
  - `typemax(Int32)`
  - Maximum number of iterations allowed.
* - `check_iter`
  - `150`
  - Number of iterations to check residuals.
* - `use_Ruiz_scaling`
  - `true`
  - Whether to apply Ruiz scaling.
* - `use_Pock_Chambolle_scaling`
  - `true`
  - Whether to use the Pock-Chambolle scaling.
* - `use_bc_scaling`
  - `true`
  - Whether to use the scaling for b and c.
* - `use_gpu`
  - `true`
  - Whether to use GPU or not.
* - `print_frequency`
  - `-1` (auto)
  - Print the log every `print_frequency` iterations.
```
---

## Result Explanation

After solving an instance, you can access the result variables as shown below:

```julia
# Example from /demo/demo_Abc.jl
println("Objective value: ", result.primal_obj)
println("x1 = ", result.x[1])
println("x2 = ", result.x[2])
```



```{list-table}
:header-rows: 1
:widths: 20 20 60

* - **Category**
  - **Variable**
  - **Description**

* - Iteration Counts
  - `iter`
  - Total number of iterations performed by the algorithm.
* - 
  - `iter_4`
  - Number of iterations required to achieve an accuracy of `1e-4`.
* - 
  - `iter_6`
  - Number of iterations required to achieve an accuracy of `1e-6`.

* - Time Metrics
  - `time`
  - Total time in seconds taken by the algorithm.
* - 
  - `time_4`
  - Time in seconds taken to achieve an accuracy of `1e-4`.
* - 
  - `time_6`
  - Time in seconds taken to achieve an accuracy of `1e-6`.
* - 
  - `power_time`
  - Time in seconds used by the power method.

* - Objective Values
  - `primal_obj`
  - The primal objective value obtained.
* - 
  - `gap`
  - The gap between the primal and dual objective values.

* - Residuals
  - `residuals`
  - Relative residuals of the primal feasibility, dual feasibility, and duality gap.

* - Algorithm Status
  - `output_type`
  - The final status of the algorithm:
    - `OPTIMAL` : Found optimal solution
    - `MAX_ITER` : Max iterations reached
    - `TIME_LIMIT` : Time limit reached

* - Solution Vectors
  - `x`
  - The final solution vector **x**.
* - 
  - `y`
  - The final solution vector **y**.
* - 
  - `z`
  - The final solution vector **z**.
```


That’s it! With these steps you can run demos, build your own LPs, tune solver settings, and interpret results in Julia.