# Python Version
<!-- Coming soon... -->
This page shows how to use the **Python interface** of HPR-LP: run demos, build custom problems, adjust solver settings, and interpret results.

---

## Running examples

The demo LP problem is:

### Test problem (LP)

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

After installing the environment, you can run the solver in two ways: **model-based API** or **`.mps` API**.

### 1. Model-based API 

You can also build and solve a small demo script under `demo/demo_model_api.py`.

```bash
python demo/demo_model_api.py
```

### 2. MPS file API

```bash
python scripts/run_single_file.py
```

This calls `run_single_file.py` with its default arguments, which solve one LP model in MPS format.

You can also override any of these from the command line, for example:

```bash
python scripts/run_single_file.py \
    --file_name /path/to/your_problem.mps \
    --device_number 0 \
    --stoptol 1e-8 \
    --time_limit 3600 \
    --check_iter 150 \
    --warm_up True \
    --use_Ruiz_scaling True \
    --use_Pock_Chambolle_scaling True \
    --use_bc_scaling True
```

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


## Results
After solving an instance, you can access the result variables as shown below:

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
