# Benchmarks

This page reports numerical results of Julia version on an **NVIDIA A100-SXM4-80GB** GPU.

---

## 1) Mittelmann LP benchmark set 

Numerical performance of **HPR-LP.jl** and [<u>**cuPDLP.jl**</u>](https://github.com/jinwen-yang/cuPDLP.jl) (downloaded on July 24th, 2024) on 49 instances of [<u>Mittelmann’s LP benchmark set</u>](https://plato.asu.edu/ftp/lpfeas.html) with Gurobi’s presolve. Time limit **15,000 seconds**.

| Tolerance | 1e-4 | 1e-4 | 1e-6 | 1e-6 | 1e-8 | 1e-8 |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| **Solvers** | **SGM10** | **Solved** | **SGM10** | **Solved** | **SGM10** | **Solved** |
| cuPDLP.jl | 76.9 | 42 | 156.2 | 41 | 277.9 | 40 |
| HPR-LP.jl (v0.1.0) | 30.2 | 47 | 69.1 | 44 | 103.8 | 43 |
| HPR-LP.jl (v0.1.2) | 25.7 | 47 | 53.2 | 44 | 82.1 | 44 |

---

## 2) MIPLIB 2017 LP relaxations 

Numerical performance of **HPR-LP.jl** and **cuPDLP.jl** on 18 LP relaxations (>10M nonzeros in `A`) from [<u>MIPLIB 2017</u>](https://miplib.zib.de/) without Gurobi’s presolve. Time limit **18,000 seconds**.

| Tolerance | 1e-4 | 1e-4 | 1e-6 | 1e-6 | 1e-8 | 1e-8 |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| **Solvers** | **SGM10** | **Solved** | **SGM10** | **Solved** | **SGM10** | **Solved** |
| cuPDLP.jl | 129.8 | 16 | 253.3 | 15 | 442.2 | 14 |
| HPR-LP.jl (v0.1.0) | 117.6 | 17 | 260.7 | 15 | 428.6 | 14 |
| HPR-LP.jl (v0.1.2) | 60.9 | 17 | 122.5 | 17 | 204.2 | 17 |

---

