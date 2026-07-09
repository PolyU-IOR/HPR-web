# Pure C examples from C programs

Pure C examples demonstrating how to use HPR-LP from C programs.

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

## Examples

**example_direct_lp.c** - Solve LP from arrays in CSR format
```bash
make example_direct_lp
./example_direct_lp
```

**example_mps_file.c** - Solve LP from MPS file
```bash
make example_mps_file
./example_mps_file
```

## Building

Build the HPRLP library first:
```bash
cd ../..
make
make shared   # Build shared library for dynamic linking
```

Then build and run examples:
```bash
cd examples/c
make          # Build all examples
make run      # Build and run all examples
```

Or build and run individual examples:
```bash
make example_direct_lp
./example_direct_lp

make example_mps_file
./example_mps_file
```

**Note:** The Makefile will automatically build `libhprlp.so` if it doesn't exist, but if you get a "cannot open shared object file" error, run `make shared` in the project root first.

## Basic Usage

```c
#include "HPRLP.h"

// Create model from arrays (CSR format)
LP_info_cpu* model = create_model_from_arrays(
    m, n, nnz,
    rowPtr, colIndex, values,
    AL, AU, l, u, c,
    false  // is_csc=false for CSR format
);

// Or create a model from the MPS file
LP_info_cpu* model = create_model_from_mps("model.mps");

// Solve the model with custom parameters
HPRLP_parameters param;
param.stop_tol = 1e-9;
param.device_number = 0;
HPRLP_results result = solve(model, &param);

// Access solution
if (result.x != NULL) {
    // Use result.x (primal solution)
    // Use result.y (dual solution)
    
    // Free solution arrays
    free(result.x);
    free(result.y);
}

// Free the model
free_model(model);
```

