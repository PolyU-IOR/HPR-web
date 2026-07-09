# Benchmarks

This page reports numerical results on an **NVIDIA A100-SXM4-80GB** GPU.

---

## Numerical Results

- **HPR-QP** is implemented in Julia and leverages CUDA for GPU acceleration.  
- [**PDQP**](https://github.com/jinwen-yang/PDQP.jl) (GPU, downloaded in April 2025).  
- [**SCS**](https://github.com/jump-dev/SCS.jl) (GPU, v2.1.0)is written in C/C++ with a Julia interface. GPU acceleration is enabled via its indirect solver, which performs all matrix operations on the GPU.  
- [**CuClarabel**](https://github.com/oxfordcontrol/Clarabel.jl/tree/CuClarabel) (GPU, v0.10.0).  
- [**Gurobi**](https://www.gurobi.com/) (CPU, version 12.0.2, academic license) is executed on CPU using the barrier method.  
- All benchmarks were conducted on a SuperServer SYS-420GP-TNR with an NVIDIA A100-SXM4-80GB GPU, Intel Xeon Platinum 8338C CPU @ 2.60 GHz, and 256 GB RAM

---

## Maros–Mészáros Data Set (137 Instances; tolerances $10^{-6}$ and $10^{-8}$)

| Solver | SGM10 (1e-6) | Solved (1e-6) | SGM10 (1e-8) | Solved (1e-8) |
|:--|--:|--:|--:|--:|
| **HPR-QP**       | 10.5 | 129 | 12.6 | 128 |
| **PDQP**         | 33.1 | 125 | 42.5 | 124 |
| **SCS**          | 126.0 | 103 | 165.0 | 93 |
| **CuClarabel**   | 3.7 | 130 | 7.8 | 124 |
| **Gurobi**       | 0.4 | 137 | 1.2 | 135 |

---

## QAP Relaxations (36 Instances; tolerances $10^{-6}$ and $10^{-8}$)

| Solver | SGM10 (1e-6) | Solved (1e-6) | SGM10 (1e-8) | Solved (1e-8) |
|:--|--:|--:|--:|--:|
| **HPR-QP**       | 1.8 | 36 | 4.7 | 36 |
| **PDQP**         | 124.1 | 23 | 149.4 | 23 |
| **SCS**          | 11.3 | 36 | 86.0 | 36 |
| **CuClarabel**   | 13.6 | 33 | 114.9 | 22 |
| **Gurobi**       | 24.8 | 36 | 26.8 | 36 |

---

## LASSO Problems (11 Instances; tolerance $10^{-8}$)

**Abbreviations:** `T` = time-limit, `F` = failure (e.g., unbounded or infeasible).

| Instance | HPR-QP | PDQP | SCS | CuClarabel | Gurobi |
|:--|--:|--:|--:|--:|--:|
| abalone7            | 10.5 | 372.5 | T     | 24.4 | 127.3 |
| bodyfat7            | 1.2  | 33.3  | T     | 2.2  | 30.8  |
| E2006.test          | 0.2  | 1.3   | T     | 15.4 | 9.0   |
| E2006.train         | 0.7  | 1.9   | F     | 116.0| 277.8 |
| housing7            | 22.6 | 123.3 | T     | 5.7  | 125.9 |
| log1p.E2006.test    | 7.0  | 1416.9| T     | 196.0| 137.0 |
| log1p.E2006.train   | 17.3 | 2983.2| T     | 361.0| 878.8 |
| mpg7                | 0.6  | 18.1  | 2000.0| 0.3  | 1.2   |
| pyrim5              | 49.1 | 410.6 | T     | 3.5  | 35.9  |
| space_ga9           | 0.6  | 62.7  | 1210.0| 6.7  | 38.1  |
| triazines4          | 401.3| 3533.3| T     | 26.0 | 843.1 |
| **SGM10 (time)**    | **13.2** | **161.8** | **3091.0** | **26.1** | **91.2** |

