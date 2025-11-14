# About HPR-QP

HPR-QP is a GPU-accelerated solver for large-scale convex composite quadratic programming (CCQP). It is a GPU-based dual Halpern–Peaceman–Rachford solver built on the restricted Wolfe dual with symmetric Gauss–Seidel, range-space updates, and adaptive restart.

## Problem statement


**Problem form.** The CCQP solved by HPR-QP is:

```{math}
\begin{aligned}
\min_{x \in \mathbb{R}^n}\quad & \tfrac12\langle x, Qx\rangle + \langle c, x \rangle + \phi(x) \\
\text{s.t.}\quad & Ax \in \mathcal{K}, \\
\end{aligned}
```

where $Q:\mathbb{R}^n\to\mathbb{R}^n$ is a self-adjoint positive semidefinite linear operator, 
$c\in\mathbb{R}^n$ is a given vector, and $\phi:\mathbb{R}^n\to(-\infty,+\infty]$ is a proper, closed, and convex function.  
Here, $A:\mathbb{R}^n\to\mathbb{R}^m$ is a linear operator, and $\mathcal{K}$ is a simple polyhedral set:


```{math}
\mathcal{K} := \{\, y \in \mathbb{R}^m \mid -\infty \le l_i \le y_i \le u_i \le +\infty,\; 1 \le i \le m \,\}.
```

A key feature of our approach is that it does not require an explicit matrix representation of $Q$,  
which makes the proposed method particularly suitable for large-scale or matrix-free settings—e.g., when $Q$ is defined implicitly via Kronecker products or structured operators.

In particular, CCQP includes the classical convex QP (CQP) as an important special case:


```{math}
\begin{aligned}
\min_{x \in \mathbb{R}^n}\quad & \tfrac12\langle x, Qx\rangle + \langle c, x \rangle + \delta_{\mathcal{C}}(x) \\
\text{s.t.}\quad & Ax \in \mathcal{K}, \\
\end{aligned}
```

Here, $\delta_{\mathcal{C}}(\cdot)$ is the indicator function of the box constraint set $\mathcal{C}$:

```{math}
\mathcal{C} := \{\, x \in \mathbb{R}^n \mid L \le x \le U \,\},
\qquad
L \in (\mathbb{R} \cup \{-\infty\})^n,\quad
U \in (\mathbb{R} \cup \{+\infty\})^n.
```

**Dual form.** The novel restricted Wolfe dual problem is:

```{math}
\begin{aligned}
\min_{(y,w,z) \in \mathbb{R}^m \times \mathbb{R}^n \times \mathbb{R}^n} \quad
& \tfrac{1}{2}\langle w, Qw\rangle
  + \delta_{\mathcal{K}}^*(-y)
  + \phi^*(-z) \\
\text{s.t.} \quad
& -Qw + A^*y + z = c, \\
& w \in \mathcal{W}.
\end{aligned}
```

where $\mathcal{W}:=Range(Q)$, the range space of $Q$.



## Dual HPR method for Solving CCQP

HPR-QP is based on the Halpern–Peaceman–Rachford (HPR) method for convex composite quadratic programming (CCQP). It's a general HPR framework with semi-proximal terms for solving the restricted Wolfe dual problem. The base algorithm appears below, followed by its convergence guarantees and complexity properties, which in turn motivate the algorithmic enhancements described later.


### Base algorithm

Let $\sigma > 0$ be a given penalty parameter.  
Define the augmented Lagrangian function $L_{\sigma}(y,w,z; x)$ associated with problem for any  
$(y,w,z,x) \in \mathbb{R}^m \times \mathcal{W} \times \mathbb{R}^n \times \mathbb{R}^n$ as follows:

```{math}
L_{\sigma}(y,w,z; x)
= \tfrac{1}{2}\langle w, Qw\rangle
  + \delta_{\mathcal{K}}^*(-y)
  + \phi^*(-z)
  + \langle x, -Qw + A^*y + z - c\rangle
  + \tfrac{\sigma}{2}\| -Qw + A^*y + z - c \|^2.
```

We make the following assumption:

**Assumption 1** *There exists a vector $(y^*, w^*, z^*, x^*) \in \mathbb{R}^m \times \mathcal{W} \times \mathbb{R}^n \times \mathbb{R}^n$ satisfying the KKT system.*


```{math}
\begin{array}{|l|}
\hline
\textbf{Algorithm 1: A dual HPR method for solving the restricted-Wolfe dual problem} \\ \hline
\textbf{Input:}\ 
\text{Let } \mathcal{S}_y \text{ and } \mathcal{S}_w \text{ be two self-adjoint positive semidefinite linear operators on } \mathbb{R}^m \text{ and } \mathcal{W}, \\
\text{respectively, such that } \mathcal{S}_y + A A^* \text{ is positive definite. Denote } u = (y, w, z, x), \ \bar{u} = (\bar{y}, \bar{w}, \bar{z}, \bar{x}). \\
\text{Let } u^0 = (y^0, w^0, z^0, x^0) \in \mathcal{U}, \ \text{and set } \sigma > 0. \\ 
\textbf{for } k = 0,1,2,\ldots \ \textbf{do} \\ 
\quad \text{Step 1: } \ \bar{z}^{k+1} = \arg\min_{z \in \mathbb{R}^n} \{ L_\sigma(y^k, w^k, z; x^k) \}; \\[3pt]
\quad \text{Step 2: } \ \bar{x}^{k+1} = x^k + \sigma(-Qw^k + A^*y^k + \bar{z}^{k+1} - c); \\[3pt]
\quad \text{Step 3-1: } \ \bar{w}^{k+\frac{1}{2}} = \arg\min_{w \in \mathcal{W}} 
   \{ L_\sigma(y^k, w, \bar{z}^{k+1}; \bar{x}^{k+1}) + \tfrac{\sigma}{2}\| w - w^k \|_{\mathcal{S}_w}^2 \}; \\[3pt]
\quad \text{Step 3-2: } \ \bar{y}^{k+1} = \arg\min_{y \in \mathbb{R}^m}
   \{ L_\sigma(y, \bar{w}^{k+\frac{1}{2}}, \bar{z}^{k+1}; \bar{x}^{k+1}) + \tfrac{\sigma}{2}\| y - y^k \|_{\mathcal{S}_y}^2 \}; \\[3pt]
\quad \text{Step 3-3: } \ \bar{w}^{k+1} = \arg\min_{w \in \mathcal{W}}
   \{ L_\sigma(\bar{y}^{k+1}, w, \bar{z}^{k+1}; \bar{x}^{k+1}) + \tfrac{\sigma}{2}\| w - w^k \|_{\mathcal{S}_w}^2 \}; \\[3pt]
\quad \text{Step 4: } \ \hat{u}^{k+1} = 2\bar{u}^{k+1} - u^k; \\[3pt]
\quad \text{Step 5: } \ u^{k+1} = \tfrac{1}{k+2}u^0 + \tfrac{k+1}{k+2}\hat{u}^{k+1}; \\ 
\textbf{end for} \\ 
\textbf{Output:}\ \text{Iteration sequence } \{ \bar{u}^k \}. \\ \hline
\end{array}
```
**Remark** In Algorithm 1, the updates for $\bar{w}^{k+\frac{1}{2}}$ and $\bar{w}^{k+1}$ for $k \ge 0$ are restricted to the subspace $\mathcal{W} = \mathrm{Range}(Q)$. Although it may seem more straightforward to update $\bar{w}^{k+\frac{1}{2}}$ and $\bar{w}^{k+1}$ in the full space $\mathbb{R}^n$, doing so—particularly under a linearized ADMM framework—necessitates a proximal operator with a larger spectral norm, such as  
$\mathcal{S}_w = \lambda_1(Q^2 + Q/\sigma)I_n - (Q^2 + Q/\sigma)$, to ensure convergence.  
A proximal operator with a large spectral norm typically results in slower convergence.  
By contrast, restricting the update to $\mathcal{W}$ allows *HPR-QP* to employ a proximal operator with a smaller spectral norm, namely  
$\mathcal{S}_w = Q(\lambda_1(Q)I_n - Q)$, which accelerates convergence while preserving theoretical guarantees.


### An Easy-to-Implement Dual HPR Method

While computing $\bar{w}^{k+\frac{1}{2}}$ and $\bar{w}^{k+1}$ within $\mathrm{Range}(Q)$ may seem costly, these updates can be implemented efficiently **without explicit projection**. For small-scale or structured cases, one may simply set $\mathcal{S}_w = 0$ and use direct or preconditioned conjugate gradient solvers.  For large-scale general CCQP problems, HPR-QP adopts the proximal operator
```{math}
\mathcal{S}_w = Q(\lambda_Q I_n - Q),
```
where $\lambda_Q > 0$ satisfies $\lambda_Q \ge \lambda_1(Q)$. Then, for $k \ge 0$, the updates of $\bar{w}^{k+\frac{1}{2}}$ and $\bar{w}^{k+1}$ become
```{math}
\left\{
\begin{aligned}
Q\bar{w}^{k+\frac{1}{2}}
&= \frac{1}{1+\sigma\lambda_Q}\,
  Q\!\left(\sigma\lambda_Q w^k + \bar{x}^{k+1}
  + \sigma(-Qw^k + A^* y^k + \bar{z}^{k+1} - c)\right),
  \quad \bar{w}^{k+\frac{1}{2}} \in \mathcal{W},
  \\
Q\bar{w}^{k+1}
&= \frac{1}{1+\sigma\lambda_Q}\,
  Q\!\left(\sigma\lambda_Q w^k + \bar{x}^{k+1}
  + \sigma(-Qw^k + A^* \bar{y}^{k+1} + \bar{z}^{k+1} - c)\right),
  \quad \bar{w}^{k+1} \in \mathcal{W}.
\end{aligned}
\right.
```


This design allows efficient updates via a **shadow sequence**, avoiding explicit projection onto $\mathrm{Range}(Q)$ and reducing computational overhead.

```{math}
\begin{array}{|l|}
\hline
\textbf{Algorithm 2: An easy-to-implement dual HPR method}\\ \textbf{for the restricted-Wolfe dual problem} \\ \hline
\textbf{Input:}\ 
\text{Let } \mathcal{S}_w = Q(\lambda_Q I_n - Q) \text{ with } \lambda_Q \ge \lambda_1(Q), \text{ and let } \mathcal{S}_y \succeq 0 \text{ such that } \mathcal{S}_y + A A^* \succ 0. \\ 
\text{Denote } u_Q = (y, w_Q, z, x),\ \bar{u}_Q = (\bar{y}, \bar{w}_Q, \bar{z}, \bar{x}).\ \text{Let } u_Q^0 = (y^0, w_Q^0, z^0, x^0) \text{ and set } \sigma > 0. \\ 
\textbf{for } k = 0,1,2,\ldots \ \textbf{do} \\ 
\quad \text{Step 1: } \ \bar{z}^{k+1} = \arg\min_{z \in \mathbb{R}^n} \{ L_\sigma(y^k, w_Q^k, z; x^k) \}; \\[3pt]
\quad \text{Step 2: } \ \bar{x}^{k+1} = x^k + \sigma(-Qw_Q^k + A^*y^k + \bar{z}^{k+1} - c); \\[3pt]
\quad \text{Step 3-1: } \ \bar{w}_Q^{k+\frac{1}{2}} = \tfrac{1}{1+\sigma\lambda_Q}
  (\sigma\lambda_Q w_Q^k + \bar{x}^{k+1} + \sigma(-Qw_Q^k + A^*y^k + \bar{z}^{k+1} - c)); \\[3pt]
\quad \text{Step 3-2: } \ \bar{y}^{k+1} = \arg\min_{y \in \mathbb{R}^m}
  \{ L_\sigma(y, \bar{w}_Q^{k+\frac{1}{2}}, \bar{z}^{k+1}; \bar{x}^{k+1}) + \tfrac{\sigma}{2}\|y - y^k\|_{\mathcal{S}_y}^2 \}; \\[3pt]
\quad \text{Step 3-3: } \ \bar{w}_Q^{k+1} = \tfrac{1}{1+\sigma\lambda_Q}
  (\sigma\lambda_Q w_Q^k + \bar{x}^{k+1} + \sigma(-Qw_Q^k + A^*\bar{y}^{k+1} + \bar{z}^{k+1} - c)); \\[3pt]
\quad \text{Step 4: } \ \hat{u}_Q^{k+1} = 2\bar{u}_Q^{k+1} - u_Q^k; \\[3pt]
\quad \text{Step 5: } \ u_Q^{k+1} = \tfrac{1}{k+2}u_Q^0 + \tfrac{k+1}{k+2}\hat{u}_Q^{k+1}; \\ 
\textbf{end for} \\ 
\textbf{Output:}\ \text{Iteration sequence } \{ \bar{u}_Q^k \}. \\ \hline
\end{array}
```


**Theorem 1** *Suppose Assumption 1 holds.  
Let $\{\bar{u}_Q^k\} = \{(y^k, w_Q^k, z^k, x^k)\}$ and $\{u_Q^k\} = \{(y^k, w_Q^k, z^k, x^k)\}$ be the sequences generated by Algorithm&nbsp;2,  
and let $u^* = (y^*, w^*, z^*, x^*)$ be a solution to the KKT system.  
Then, for all $k \ge 0$, the following complexity bounds hold with $R_0 = \|u_Q^0 - u^*\|_{\mathcal{M}}$:*

```{math}
\|\bar{u}_Q^{k+1} - u_Q^k\|_{\mathcal{M}} \le \frac{R_0}{k+1},
```

```{math}
\|\mathcal{R}(\bar{u}_Q^{k+1})\|
\le \left(\frac{\sigma\|A_Q^*\| + 1}{\sqrt{\sigma}} + \|\sqrt{\mathcal{S} + \hat{\mathcal{S}}_{\mathrm{sGS}}}\|\right)\frac{R_0}{k+1},
```

```{math}
-\frac{\|x^*\|}{\sqrt{\sigma}} \cdot \frac{R_0}{k+1}
\;\le\;
h(\bar{y}^{k+1}, \bar{w}_Q^{k+1}, \bar{z}^{k+1})
\;\le\;
\left(3R_0 + \frac{\|x^*\|}{\sqrt{\sigma}}\right)\frac{R_0}{k+1}.
```



```{math}
\begin{array}{|l|}
\hline
\textbf{Algorithm 3: HPR-QP — A dual HPR method for the CCQP problem} \\ \hline
\textbf{Input: }
\text{Let }\mathcal{S}_w\text{ be defined as in (2.8), and let }\mathcal{S}_y\text{ be a self-adjoint positive semidefinite linear operator on }\mathbb{R}^m,\\
\text{such that }\mathcal{S}_y + A A^*\text{ is positive definite. Let }u_Q=(y,w_Q,z,x),\ \bar{u}_Q=(\bar{y},\bar{w}_Q,\bar{z}_Q,\bar{x}),\\
\text{and initial point }u_Q^{0,0}=(y^{0,0},w_Q^{0,0},z^{0,0},x^{0,0})\in\mathbb{R}^m\times\mathbb{R}^n\times\mathbb{R}^n\times\mathbb{R}^n.\\[0.4em]
\textbf{Initialization: }
\text{Set outer loop counter }r=0,\ \text{total iteration counter }k=0,\ \text{and initial penalty parameter }\sigma_0>0.\\[0.4em]
\textbf{repeat} \\
\quad \text{Initialize inner loop: set inner counter }t=0;\\
\quad \textbf{repeat} \\
\quad\quad \bar{z}_Q^{r,t+1}
= \operatorname*{arg\,min}_{z\in\mathbb{R}^n}\, L_{\sigma_r}(y^{r,t}, w_Q^{r,t}, z;\ x^{r,t});\\
\quad\quad \bar{x}^{r,t+1}
= x^{r,t} + \sigma_r\!\left(-Q w_Q^{r,t} + A^* y^{r,t} + \bar{z}_Q^{r,t+1} - c\right);\\
\quad\quad \bar{w}_Q^{r,t+\frac{1}{2}}
= \frac{1}{1+\sigma_r \lambda_Q}\!\left(\sigma_r \lambda_Q w_Q^{r,t} + \bar{x}^{r,t+1}
+ \sigma_r\!\left(-Q w_Q^{r,t} + A^* y^{r,t} + \bar{z}_Q^{r,t+1} - c\right)\right);\\
\quad\quad \bar{y}^{r,t+1}
= \operatorname*{arg\,min}_{y\in\mathbb{R}^m}
\Big\{ L_{\sigma_r}\!\left(y, \bar{w}_Q^{r,t+\frac{1}{2}}, \bar{z}_Q^{r,t+1};\ \bar{x}^{r,t+1}\right)
+ \tfrac{\sigma_r}{2}\,\|y - y^{r,t}\|_{\mathcal{S}_y}^2 \Big\};\\
\quad\quad \bar{w}_Q^{r,t+1}
= \frac{1}{1+\sigma_r \lambda_Q}\!\left(\sigma_r \lambda_Q w_Q^{r,t} + \bar{x}^{r,t+1}
+ \sigma_r\!\left(-Q w_Q^{r,t} + A^* \bar{y}^{r,t+1} + \bar{z}_Q^{r,t+1} - c\right)\right);\\
\quad\quad \hat{u}_Q^{r,t+1} = 2\,\bar{u}_Q^{r,t+1} - u_Q^{r,t};\\
\quad\quad u_Q^{r,t+1} = \tfrac{1}{t+2}\,u_Q^{r,0} + \tfrac{t+1}{t+2}\,\hat{u}_Q^{r,t+1};\\
\quad\quad t = t + 1,\ \ k = k + 1;\\
\quad \textbf{until restart or termination criteria are met;}\\[0.3em]
\quad \textbf{Restart: }
\text{Set }\tau_r = t,\ \ u_Q^{r+1,0} = \bar{u}_Q^{r,\tau_r};\\
\quad \sigma_{r+1} = \textbf{SigmaUpdate}\!\left(\bar{u}_Q^{r,\tau_r},\ u_Q^{r,0},\ \mathcal{S}_y,\ \mathcal{S}_w,\ A,\ Q\right);\\
\quad r = r + 1;\\
\textbf{until termination criteria are met;}\\
\textbf{Output: } \{\bar{u}_Q^{r,t}\}.\\ \hline
\end{array}
```




### Restart strategy


HPR-QP method adopts an adaptive restart strategy grounded in the $O(1/k)$ iteration complexity of the HPR method. This strategy has shown strong empirical performance on large-scale convex problems.  
Motivated by this success, we extend the adaptive restart strategy to the CCQP problem by defining a merit function consistent with the theoretical complexity bound. Specifically, we define the following idealized merit function:

```{math}
R_{r,t} := \| u_Q^{r,t} - u^* \|_{\mathcal{M}}, 
\qquad \forall\, r \ge 0,\ t \ge 0,
```

where $u^*$ denotes any solution to the KKT system. Note that $R_{r,0}$ corresponds to the upper bound implied by the complexity result at the beginning of the $r$-th outer iteration. Since $u^*$ is unknown in practice, we use the following computable surrogate:

```{math}
\tilde{R}_{r,t} := \| u_Q^{r,t} - \hat{u}_Q^{r,t+1} \|_{\mathcal{M}}.
```

Based on this surrogate merit function, we introduce the following adaptive restart criteria for HPR-QP method:

1. **Sufficient decay:**

```{math}
\tilde{R}_{r,t+1} \le \alpha_1\, \tilde{R}_{r,0};
```

2. **Insufficient local progress despite overall decay:**

```{math}
\tilde{R}_{r,t+1} \le \alpha_2\, \tilde{R}_{r,0}, 
\qquad
\tilde{R}_{r,t+1} > \tilde{R}_{r,t};
```

3. **Excessively long inner loop:**

```{math}
t \ge \alpha_3\, k;
```

where $\alpha_1 \in (0, \alpha_2)$, $\alpha_2 \in (0,1)$, and $\alpha_3 \in (0,1)$ are user-defined parameters. Whenever any of the above conditions is satisfied, the current inner loop is terminated, and a new outer iteration is started by setting $u_Q^{r+1,0} = \bar{u}_Q^{r,\tau_r}$ and updating the penalty parameter $\sigma_{r+1}$ accordingly.




### Update strategy for $\sigma$

The penalty parameter $\sigma$ is dynamically updated at each restart to improve convergence stability and reduce the residual of the KKT system. At the beginning of the $(r+1)$-th outer iteration, the ideal update rule is defined by

```{math}
\sigma_{r+1}
:= \operatorname*{arg\,min}_{\sigma > 0}
\| u_Q^{r+1,0} - u^* \|_{\mathcal{M}}^2,
```

where $u^*$ denotes any solution to the KKT system and $\|u_Q^{r+1,0} - u^*\|_{\mathcal{M}}$ corresponds to the upper bound. Since $u^*$ is unknown in practice, we approximate the above rule by minimizing a computable surrogate function

```{math}
f(\sigma)
= \tilde{\theta}_1\,\sigma
  + \frac{\tilde{\theta}_2}{\sigma}
  + \frac{\sigma^2 \tilde{\theta}_3}{1 + \lambda_Q \sigma},
```

where the coefficients are estimated from observable quantities of the current and previous restarts:
```{math}
\tilde{\theta}_1 = \lambda_A \| \bar{y}^{r,\tau_r} - y^{r,0} \|^2
                 + \lambda_Q \| \bar{w}_Q^{r,\tau_r} - w_Q^{r,0} \|_Q^2,
\qquad
\tilde{\theta}_2 = \| \bar{x}^{r,\tau_r} - x^{r,0} \|^2,
\qquad
\tilde{\theta}_3 = \| A^*\bar{y}^{r,\tau_r} - A^*y^{r,0} \|_Q^2.
```

This one-dimensional minimization problem can be efficiently solved using a golden-section search or other scalar optimization methods to obtain $\sigma_{\text{new}}$. To stabilize the update, an exponential smoothing scheme is applied:

```{math}
\sigma_{r+1}
= \exp\!\big(
  \beta \log(\sigma_{\text{new}})
  + (1-\beta)\log(\sigma_r)
\big),
\qquad
\beta = \exp\!\left(-\frac{\tilde{R}_{r,\tau_r-1}}{\tilde{R}_{r,0}-\tilde{R}_{r,\tau_r-1}}\right),
```

where $\tilde{R}_{r,t}$ is the surrogate merit function defined in the restart criteria. This adaptive update balances theoretical consistency and empirical stability, ensuring smooth adjustment of $\sigma$ throughout the optimization process.



## GPU Implementation

We now present the GPU-oriented update formulas for each subproblem in **HPR-QP**.  
For any $r \ge 0$ and $t \ge 0$, the update of $\bar{z}_Q^{r,t+1}$ is:

```{math}
\bar{z}_Q^{r,t+1}
= \frac{1}{\sigma_r}
\Big(
  \operatorname{Prox}_{\sigma_r \phi}(r_{z}^{r,t})
  - r_{z}^{r,t}
\Big),
\qquad
r_{z}^{r,t} = x^{r,t} + \sigma_r(-Qw_Q^{r,t} + A^*y^{r,t} - c).
```

The corresponding update of $\bar{x}^{r,t+1}$ is then given by:

```{math}
\bar{x}^{r,t+1}
= x^{r,t}
+ \sigma_r(-Qw_Q^{r,t} + A^*y^{r,t} + \bar{z}_Q^{r,t+1} - c)
= \operatorname{Prox}_{\sigma_r \phi}(r_{z}^{r,t}).
```

Next, the updates of $\bar{w}_Q^{r,t+\frac{1}{2}}$ and $\bar{w}_Q^{r,t+1}$ can be simplified as

```{math}
\begin{aligned}
\bar{w}_Q^{r,t+\frac{1}{2}}
&= \frac{1}{1+\sigma_r \lambda_Q}
\Big(
  \sigma_r \lambda_Q w_Q^{r,t}
  + \bar{x}^{r,t+1}
  + \sigma_r(-Qw_Q^{r,t} + A^*y^{r,t} + \bar{z}_Q^{r,t+1} - c)
\Big),\\[4pt]
\bar{w}_Q^{r,t+1}
&= \frac{1}{1+\sigma_r \lambda_Q}
\Big(
  \sigma_r \lambda_Q w_Q^{r,t}
  + \bar{x}^{r,t+1}
  + \sigma_r(-Qw_Q^{r,t} + A^*\bar{y}^{r,t+1} + \bar{z}_Q^{r,t+1} - c)
\Big)\\[4pt]
&= \bar{w}_Q^{r,t+\frac{1}{2}}
  + \frac{\sigma_r}{1+\sigma_r \lambda_Q}
    A^*(\bar{y}^{r,t+1} - y^{r,t}).
\end{aligned}
```

To simplify the subproblem with respect to $y$, we adopt the proximal operator

```{math}
\mathcal{S}_y = \lambda_A I_m - A A^*,
\qquad
\lambda_A \ge \|A\|_2^2.
```

With this choice, the $y$-update reduces to the projection

```{math}
\bar{y}^{r,t+1}
= \frac{1}{\sigma_r \lambda_A}
\Big(
  \Pi_{\mathcal{K}}(R_y) - R_y
\Big),
\qquad
R_y := A(2\bar{x}^{r,t+1} - x^{r,t}) - \sigma_r \lambda_A y^{r,t}.
```

Each step thus consists only of **sparse matrix–vector products (SpMV)**, vector additions, and simple proximal/projection operations, giving a per-iteration complexity of $O(\mathrm{nnz}(A))$.  

On GPUs, these operations are fused into custom CUDA kernels.  
Matrix–vector multiplications are implemented with **`cusparseSpMV()`** under the **`CUSPARSE_SPMV_CSR_ALG2`** algorithm for deterministic and high-throughput performance.



