# Julia Releases
A compact index of HPR-LP (Julia) releases—each entry shows the version tag and a one-line summary; click a version to view full notes, benchmarks, and downloads.

---



<details id="v013">
<summary><code>v0.1.3</code> — Robustness upgrade: refined parameter schedule achieves 1e-9 KKT/duality gaps and streamlines JuMP modeling</summary>

**Release date**: 2025-10-17

**Highlights**
1. Enhanced parameter adjustment strategy for significantly improved stability, achieving relative KKT and duality gap accuracy up to **1e-9**.  
2. Improved LP modeling pipeline with seamless **JuMP** integration for a smoother modeling experience.

**Benchmark results**
- **Platform**: NVIDIA A100-SXM4-80GB  
- **Dataset**: Mittelmann’s LP benchmark (no presolve)  
- **Performance**: 47 / 49 instances solved (**Tolerance**: 1e-4, **Time limit**: 3600s)  
- **Performance**: 41 / 49 instances solved (**Tolerance**: 1e-9, **Time limit**: 3600s)

**Downloads**
- [Source code (zip)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.3.zip)  
- [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.3.tar.gz)

</details>

---

<details id="v012">
<summary><code>v0.1.2</code> — SpMV & kernel rewrites</summary>

**Release date**: 2025-09-27

**Highlights**
- SpMV rewrites: added preprocessing and buffer preallocation to avoid redundant work between iterations.  
- CUDA kernel refactors: reduced memory traffic and improved occupancy.  
- Under SGM10 (1e-8 accuracy): +11% on Mittelmann’s LP benchmark set and +7% on MIP2017 large-scale LP relaxations (vs. v0.1.1).

**Downloads**
- [HPR-LP_v012_bug_fixed.zip](https://github.com/PolyU-IOR/HPR-LP/releases/download/v0.1.2/HPR-LP_v012_bug_fixed.zip)  
- [Source code (zip)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.2.zip)  
- [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.2.tar.gz)

</details>

---

<details id="v011">
<summary><code>v0.1.1</code> — Model reformulation + adaptive restart/penalty + fused kernels</summary>

**Release date**: 2025-09-09

**Highlights**
- Model reformulation. Updated the problem formulation to the new form for better stability and consistency across instances. 
- Adaptive restarts & penalty auto-tuning. A redesigned penalty parameter update rule to improve convergence speed and robustness.
- Kernel rewrites. Several CUDA kernels were refactored/fused to reduce memory traffic and improve occupancy.
- Simplified parameters. Removed sigma and sigma_fixed from the parameters.
- In terms of SGM10 (1e-8 accuracy), 14% faster for Mittelmann's LP benchmark set and 95% faster for MIP2017 large-scale LP relaxations (compared to v0.1.0).

**Downloads**
- [Source code (zip)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.1.zip)  
- [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.1.tar.gz)

</details>

---

<details id="v010">
<summary><code>v0.1.0</code> — A preliminary release: Julia GPU-accelerated HPR-LP solver</summary>

**Release date**: 2025-07-04

**Highlights**
- First public release of **HPR-LP**.  
- GPU-accelerated LP solver in Julia implementing the Halpern–Peaceman–Rachford (HPR) method.  
- Model formulation:
```{math}
\begin{aligned}
\min_{x \in \mathbb{R}^n} \quad & (c, x) \\
\text{s.t.}\quad
& A_1 x = b_1, \\
& A_2 x \ge b_2, \\
& l \le x \le u.
\end{aligned}
```

**Downloads**
- [Source code (zip)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.0.zip)  
- [Source code (tar.gz)](https://github.com/PolyU-IOR/HPR-LP/archive/refs/tags/v0.1.0.tar.gz)

</details>

---