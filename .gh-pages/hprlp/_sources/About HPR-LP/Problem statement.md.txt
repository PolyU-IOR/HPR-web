# Problem statement



## General Linear Programming (LP) Formulation

Linear programming (LP) is one of the most fundamental problems in mathematical optimization, with applications ranging from operations research and machine learning to economics and engineering. Specifically, we consider the following general form of LP:

$$
\begin{aligned}
\min_{x \in \mathbb{R}^n} & \;\; \langle c, x \rangle \\
\text{s.t.} \;\; & Ax \in \mathcal{K}, \\
& x \in \mathcal{C},
\end{aligned}

$$

where $c \in \mathbb{R}^n$ is the objective vector, $A \in \mathbb{R}^{m \times n}$ is the constraint matrix,  
$\mathcal{K} := \{ s \in \mathbb{R}^m : l_c \leq s \leq u_c \}$ with bounds $l_c \in (\mathbb{R} \cup \{-\infty\})^m$ and $u_c \in (\mathbb{R} \cup \{\infty\})^m$,  
and $\mathcal{C} := \{ x \in \mathbb{R}^n : l_v \leq x \leq u_v \}$ with bounds $l_v \in (\mathbb{R} \cup \{-\infty\})^n$ and $u_v \in (\mathbb{R} \cup \{\infty\})^n$.  

The corresponding dual problem is:

$$
\begin{aligned}
\min_{y \in \mathbb{R}^m, \; z \in \mathbb{R}^n} & \;\; \delta_{\mathcal{K}}^*(-y) + \delta_{\mathcal{C}}^*(-z) \\
\text{s.t.} \;\; & A^* y + z = c,
\end{aligned}

$$

where $\delta_S^*(\cdot)$ denotes the convex conjugate of the indicator function $\delta_S(\cdot)$ associated with a closed convex set $S$.

## From simplex and interior-point to GPU challenges

The development of algorithms for LP has been closely linked to advances in computational hardware. The first stage was dominated by CPU-oriented, factorization-based methods. Following Dantzig’s seminal simplex method in 1947 [10], simplex solvers relied on repeated updates of basis inverses or sparse LU factorizations. Despite its exponential worst-case complexity, simplex remained the dominant method in practice for nearly half a century. The introduction of Karmarkar’s algorithm in 1984 [24] marked the rise of interior-point methods, the first polynomial-time approaches that also proved effective empirically. By the 2000s, commercial solvers such as **Gurobi** [19] and **CPLEX** [23] integrated both simplex and barrier methods with highly optimized CPU-based sparse linear algebra, achieving state-of-the-art performance. However, these approaches depend heavily on sparse matrix factorizations, limiting their scalability on massively parallel architectures such as GPUs. Even GPU-accelerated interior-point solvers like CuClarabel [18,8], which leverage mixed-precision arithmetric, continue to rely on direct factorizations and thus face challenges on very large problems.


## The rise of first-order methods

In contrast, first-order methods (FOMs) have emerged as a promising alternative for large-scale LPs due to their low per-iteration cost and high degree of parallelism. Representative LP solvers include **PDLP** [1, 2], **ECLIPSE** [3], **ABIP** [27, 12] and **HPR-LP** [5]. Beyond LP, FOM-based algorithms have also been developed for more general convex quadratic optimization, such as **SCS** [36, 35], **OSQP** [39], **PDQP** [29], **PDHCG** [22], and **PDCS** [28], **HPR-QP** [6]. A landmark development was **PDLP** [1], which is based on the primal–dual hybrid gradient (PDHG) method [45] and incorporates practical enhancements such as restarts, adaptive penalty updates, and line search. Its GPU implementations (**cuPDLP.jl** [31], **cuPDLP-c** [33], and **cuOpt** [?]) have demonstrated competitive performance against commercial solvers on large-scale instances. Notably, PDLP won the 2024 Beale–Orchard–Hays Prize for Excellence in Computational Mathematical Programming.  

Theoretically, ergodic sequences of semi-proximal ADMM (sPADMM)—which include PDHG [4, 13, 14]—achieve an $O(1/k)$ complexity in terms of objective error and feasibility violation [9]. However, whether such ergodic averages guarantee an $O(1/k)$ rate for the KKT residual in LP remains an open question; existing results [38, 34] suggest only an $O(1/\sqrt{k})$ rate in general.


