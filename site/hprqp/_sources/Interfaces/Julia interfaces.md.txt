# Julia Version

This page shows how to use the **Julia interface** of HPR-QP: run demos (MPS / MAT), build custom convex quadratic programs (CQP), and solve QAP/LASSO instances.

---

## Usage 1: Test Instances in MPS (and MAT for QAP/LASSO)

### Setting Data and Result Paths
Before running the scripts, modify `demo/run_single_file.jl` or `demo/run_dataset.jl` to set your **data path** and **result path**.

### Running a Single Instance
To test a single instance:
```bash
julia --project demo/run_single_file.jl
```

### Running All Instances in a Directory
To process all files in a directory:
```bash
julia --project demo/run_dataset.jl
```

### Notes
- **QAP instances (MAT):** The `.mat` file should include the matrices **A**, **B**, **S**, **T**.  
  See `HPR-QP_QAP_LASSO/demo/demo_QAP.jl` for how to generate such files. (Also refer to **Section 4.5** of the paper.)
- **LASSO instances (MAT):** The `.mat` file should contain matrix **A** and vector **b**.

---

## Usage 2: Define your CQP Model in Julia Scripts

### Example 1: Build & export a CQP with **JuMP**, then solve via HPR-QP

This example demonstrates how to construct a CQP model using the JuMP modeling language in Julia and export it to MPS format for use with the HPR-QP solver.

```bash
julia --project demo/demo_JuMP.jl
```
The script:
- Builds a CQP model.  
- Saves the model as an **MPS** file  
- Uses **HPR-QP** to solve the CQP instance

**Remark:** If a model may be infeasible/unbounded, you can check it with HiGHS.
```julia
using JuMP, HiGHS

# Read a model from file (or create it elsewhere)
mps_file_path = "xxx"  # your file path
model = read_from_file(mps_file_path)

# Set HiGHS as the optimizer
set_optimizer(model, HiGHS.Optimizer)

# Solve it
optimize!(model)
```

### Example 2: Define a small CQP directly in Julia (no JuMP)
This example demonstrates how to construct and solve a CQP problem directly in Julia without relying on JuMP.

```bash
julia --project demo/demo_QAbc.jl
```

### Example 3: Generate a random LASSO instance in Julia
This example demonstrates how to construct and solve a random LASSO instance.
```bash
julia --project demo/demo_LASSO.jl
```

---

## Note on First-Time Execution Performance

You may notice that solving a single instance — or the first instance in a dataset — appears slow. This is due to Julia’s **Just-In-Time (JIT) compilation**, which compiles code on first execution.

```{tip}
**Tip for Better Performance:**  
To reduce repeated compilation overhead, it’s recommended to run scripts from an **IDE like VS Code** or the **Julia REPL** in the terminal.
```

**Start Julia REPL with the project environment:**
```bash
julia --project
```

**Then, at the Julia REPL, run `demo/demo_QAbc.jl` (or other scripts):**
```julia
include("demo/demo_QAbc.jl")
```

```{admonition} CAUTION
If you encounter the error message:

```
Error: Error during loading of extension AtomixCUDAExt of Atomix, use Base.retry_load_extensions() to retry.
```

This is usually transient. Wait a few moments; the extension typically loads successfully on its own.
```

---
