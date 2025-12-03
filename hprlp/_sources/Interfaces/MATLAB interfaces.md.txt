# MATLAB Version
<!-- Coming soon... -->
This page shows how to use the **MATLAB interface** of HPR-LP: run demos, build custom problems, adjust solver settings, and interpret results.

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

## Usage 1: Test Instances in MPS Format

### Setting Data and Result Paths

> Before running the scripts, please modify **`run_single_file.m`** or **`run_dataset.m`** in the scripts directory to specify the data path and result path according to your setup.

### Running a Single Instance

To test the script on a single instance (`.mps` file):

```matlab
% Set parameters (optional)
params = HPRLPParameters();
params.stoptol = 1e-4;
params.time_limit = 3600;

% Solve from MPS file
results = runFile('your_problem.mps', params);

% Check results
fprintf('Status: %s\n', results.output_type);
fprintf('Objective: %.6e\n', results.primal_obj);
```

### Running All Instances in a Directory

To process all `.mps` files in a directory:

```matlab
% Configure parameters
params = HPRLPParameters();
params.stoptol = 1e-4;
params.time_limit = 600;

% Run on all files in the directory
runDataset('/path/to/mps/files', '/path/to/results', params);
```

---

## Usage 2: Define Your LP Model in MATLAB Scripts

### Example 1: Define an LP Instance Directly in MATLAB

This example demonstrates how to construct and solve a linear programming problem directly in MATLAB without relying on MPS files.

```matlab
run('demo/demo_Abc.m')
```

The script demonstrates:
- Direct matrix-based LP formulation
- Setting up the problem: `min c'*x` subject to `AL ≤ A*x ≤ AU`, `l ≤ x ≤ u`
- Solving with HPR-LP
- Accessing solution values

Example problem from the demo:
```matlab
% Define LP: min -3*x1 - 5*x2
%     s.t. -x1 - 2*x2 >= -10
%          -3*x1 - x2 >= -12
%          x1 >= 0, x2 >= 0

A = sparse([-1 -2; -3 -1]);
AL = [-10; -12];
AU = [Inf; Inf];
c = [-3; -5];
l = [0; 0];
u = [Inf; Inf];
obj_constant = 0.0;

params = HPRLPParameters();
params.stoptol = 1e-4;

result = runAbc(A, c, AL, AU, l, u, obj_constant, params);

fprintf('Objective value: %.10f\n', result.primal_obj);
fprintf('x1 = %.10f\n', full(result.x(1)));
fprintf('x2 = %.10f\n', full(result.x(2)));
```

---

## Parameters

Below is a list of the parameters in HPR-LP along with their default values and usage:

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Default Value</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>time_limit</code></td><td><code>3600</code></td><td>Maximum allowed runtime (seconds) for the algorithm.</td></tr>
    <tr><td><code>stoptol</code></td><td><code>1e-4</code></td><td>Stopping tolerance for convergence checks.</td></tr>
    <tr><td><code>max_iter</code></td><td><code>intmax</code></td><td>Maximum number of iterations allowed.</td></tr>
    <tr><td><code>check_iter</code></td><td><code>150</code></td><td>Number of iterations to check residuals.</td></tr>
    <tr><td><code>use_Ruiz_scaling</code></td><td><code>true</code></td><td>Whether to apply Ruiz scaling.</td></tr>
    <tr><td><code>use_Pock_Chambolle_scaling</code></td><td><code>true</code></td><td>Whether to use the Pock-Chambolle scaling.</td></tr>
    <tr><td><code>use_bc_scaling</code></td><td><code>true</code></td><td>Whether to use the scaling for b and c.</td></tr>
    <tr><td><code>print_frequency</code></td><td><code>-1</code> (auto)</td><td>Print the log every <code>print_frequency</code> iterations.</td></tr>
  </tbody>
</table>

---

## Result Explanation

After solving an instance, you can access the result variables as shown below:

```matlab
% Example from demo/demo_Abc.m
fprintf('Objective value: %.10f\n', result.primal_obj);
fprintf('x1 = %.10f\n', full(result.x(1)));
fprintf('x2 = %.10f\n', full(result.x(2)));
```

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Variable</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><b>Iteration Counts</b></td><td><code>iter</code></td><td>Total number of iterations performed by the algorithm.</td></tr>
    <tr><td></td><td><code>iter_4</code></td><td>Number of iterations required to achieve an accuracy of 1e-4.</td></tr>
    <tr><td></td><td><code>iter_6</code></td><td>Number of iterations required to achieve an accuracy of 1e-6.</td></tr>
    <tr><td></td><td><code>iter_8</code></td><td>Number of iterations required to achieve an accuracy of 1e-8.</td></tr>
    <tr><td><b>Time Metrics</b></td><td><code>time</code></td><td>Total time in seconds taken by the algorithm.</td></tr>
    <tr><td></td><td><code>time_4</code></td><td>Time in seconds taken to achieve an accuracy of 1e-4.</td></tr>
    <tr><td></td><td><code>time_6</code></td><td>Time in seconds taken to achieve an accuracy of 1e-6.</td></tr>
    <tr><td></td><td><code>time_8</code></td><td>Time in seconds taken to achieve an accuracy of 1e-8.</td></tr>
    <tr><td></td><td><code>power_time</code></td><td>Time in seconds used by the power method.</td></tr>
    <tr><td><b>Objective Values</b></td><td><code>primal_obj</code></td><td>The primal objective value obtained.</td></tr>
    <tr><td></td><td><code>gap</code></td><td>The gap between the primal and dual objective values.</td></tr>
    <tr><td><b>Residuals</b></td><td><code>residuals</code></td><td>Relative residuals of the primal feasibility, dual feasibility, and duality gap.</td></tr>
    <tr><td><b>Algorithm Status</b></td><td><code>output_type</code></td><td>The final status of the algorithm:<br/>- <code>OPTIMAL</code>: Found optimal solution<br/>- <code>MAX_ITER</code>: Max iterations reached<br/>- <code>TIME_LIMIT</code>: Time limit reached</td></tr>
    <tr><td><b>Solution Vectors</b></td><td><code>x</code></td><td>The final solution vector <code>x</code>.</td></tr>
    <tr><td></td><td><code>y</code></td><td>The final solution vector <code>y</code>.</td></tr>
    <tr><td></td><td><code>z</code></td><td>The final solution vector <code>z</code>.</td></tr>
  </tbody>
</table>
