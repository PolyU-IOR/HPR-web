# Solver settings

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
  - `1e-6`
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