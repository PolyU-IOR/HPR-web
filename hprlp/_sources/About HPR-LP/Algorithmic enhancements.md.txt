# Algorithmic enhancements

Several enhancements have been proposed to improve the performance of the HPR method for solving LP [5] and CCQP [6].  
In particular, restart strategies and adaptive updates of the penalty parameter $\sigma$, motivated by the $O(1/k)$ complexity results in Theorem 2.4, have proven effective.  
For completeness, we summarize the HPR-LP framework in Algorithm 2.2.

```{math}
\begin{array}{|l|}
\hline
\textbf{Algorithm 2.2 \  HPR-LP: A Halpern Peaceman-Rachford method} \\ \textbf{for the problem (1.2) (cf. [5])} \\ \hline
\textbf{Input:} \ \mathcal{T}_1:\mathbb{R}^m\to\mathbb{R}^m\ \text{be a self-adjoint positive semidefinite linear operator}  \text{such that }\mathcal{T}_1+AA^*\succ0.\ \\ \text{Denote }w=(y,z,x),\ \bar{w}=(\bar{y},\bar{z},\bar{x}).\ \text{Choose an initial point }w^{0,0}=(y^{0,0},z^{0,0},x^{0,0})\in\mathbb{R}^m\times\mathbb{R}^n\times\mathbb{R}^n. \\ 
\textbf{Initialization:}\ \text{Set the outer loop counter }r=0,\ \text{the total loop counter }k=0,\ \\ \text{and the initial penalty parameter }\sigma_0>0. \\ 
\textbf{repeat} \\ 
\quad \text{initialize the inner loop: set inner loop counter }t=0; \\ 
\quad \textbf{repeat} \\ 
\quad\quad \bar{z}^{r,t+1}=\arg\min_{z\in\mathbb{R}^n}\{L_{\sigma_r}(y^{r,t},z;x^{r,t})\}; \\ 
\quad\quad \bar{x}^{r,t+1}=x^{r,t}+\sigma_r(A^*y^{r,t}+\bar{z}^{r,t+1}-c); \\ 
\quad\quad \bar{y}^{r,t+1}=\arg\min_{y\in\mathbb{R}^m}\{L_{\sigma_r}(y,\bar{z}^{r,t+1};\bar{x}^{r,t+1})+\tfrac{\sigma_r}{2}\|y-y^{r,t}\|_{\mathcal{T}_1}^2\}; \\ 
\quad\quad \hat{w}^{r,t+1}=2\bar{w}^{r,t+1}-w^{r,t}; \\ 
\quad\quad w^{r,t+1}=\tfrac{1}{t+2}w^{r,0}+\tfrac{t+1}{t+2}\hat{w}^{r,t+1}; \\ 
\quad\quad t=t+1,\ k=k+1; \\ 
\quad \textbf{until}\ \text{one of the restart criteria holds or termination criteria hold} \\ 
\quad \textbf{restart the inner loop: }\tau_r=t,\ w^{r+1,0}=w^{r,\tau_r}, \\ 
\quad \sigma_{r+1}=\text{SigmaUpdate}(\bar{w}^{r,\tau_r},w^{r,0},\mathcal{T}_1,A),\ r=r+1; \\ 
\textbf{until}\ \text{termination criteria hold} \\ 
\textbf{Output:}\ \{w^{r,t}\}. \\ \hline
\end{array}
```





## Restart strategy

Restarting has been recognized as particularly important for Halpern iterations.  
As noted in Theorem 2.4, the complexity bound depends on the weighted distance $R_0$ between the initial point and the optimal solution. Consequently, as the iterates approach optimality, continuing to reference a distant initial anchor becomes counterproductive, whereas resetting the anchor to the current iterate helps reduce the bound and refocus the iteration near the solution.  

This observation motivates the merit function

```{math}
R_{r,t} := \| w^{r,t} - w^* \|_{\mathcal{M}}, 
\quad \forall r \geq 0,\; t \geq 0,
```

where $w^*$ is any solution of the KKT system (2.1). Since $w^*$ is unknown, the practical surrogate

```{math}
\tilde{R}_{r,t} := \| w^{r,t} - \hat{w}^{r,t+1} \|_{\mathcal{M}}
```

is employed in defining restart rules. The following criteria are commonly adopted:

1. **Sufficient decay:**

```{math}
\tilde{R}_{r,t+1} \leq \alpha_1 \tilde{R}_{r,0},
```

2. **Necessary decay + no local progress:**

```{math}
\tilde{R}_{r,t+1} \leq \alpha_2 \tilde{R}_{r,0}, 
\quad \text{and} \quad
\tilde{R}_{r,t+1} > \tilde{R}_{r,t};
```

3. **Long inner loop:**

```{math}
t \geq \alpha_3 k;
```

where $0 < \alpha_1 < \alpha_2 < 1$ and $0 < \alpha_3 < 1$.  
When any criterion is met, the inner loop is restarted at iteration $(r+1)$ with $w^{r+1,0} = \bar{w}^{r,\tau_r}$ and an updated $\sigma_{r+1}$.

**Remark 2.6.** Restart strategies are commonly used in first-order methods for LP [1, 31, 33, 32].  
For instance, PDLP adopts a normalized duality gap as the merit function [1], while subsequent works by Lu et al. [31, 33] introduced variants based on weighted KKT residuals.


## Update rules for $\sigma$

Another important enhancement of HPR methods concerns the update of the penalty parameter $\sigma$.  
The update strategy is motivated by the complexity results of the HPR method in Algorithm 2.1 (see Theorem 2.4).  
At a high level, the goal is to select $\sigma$ at each restart to tighten the complexity bound and thereby reduce the KKT residuals in subsequent iterations. Specifically, the ideal update is defined as the minimizer of the weighted distance to the optimal solution:

```{math}
\sigma_{r+1} := \arg\min_\sigma \| w^{r+1,0} - w^* \|_{\mathcal{M}}^2,
```

where $w^*$ is any solution of the KKT system (2.1).  
Substituting the definition of $\mathcal{M}$ from (2.3) leads to the closed-form expression

```{math}
\sigma_{r+1} =
\sqrt{
\frac{\| x^{r+1,0} - x^* \|^2}
{\| y^{r+1,0} - y^* \|_{T_1}^2 + \| A^*(y^{r+1,0} - y^*) \|^2}
}.
```

Since the optimal solution $(x^*, y^*)$ is unknown, practical implementations approximate these terms using the observed progress within each outer loop:

```{math}
\Delta_x := \| \bar{x}^{r,\tau_r} - x^{r,0} \|, 
\quad
\Delta_y := \sqrt{ \| \bar{y}^{r,\tau_r} - y^{r,0} \|_{T_1}^2 + \| A^*(\bar{y}^{r,\tau_r} - y^{r,0}) \|^2 },
```

which yields the implementable update rule

```{math}
\sigma_{r+1} = \frac{\Delta_x}{\Delta_y}.
```

---

Several special cases of $T_1$ have been investigated in the literature [5]:

1. **Case $T_1 = 0$.**  
   This case occurs when $l_c = u_c$, which arises in applications with special structure in $A$, such as optimal transport [43] and Wasserstein barycenter problem [44].  
   The $y$-update then reduces to solving the linear system

   ```{math}
   A A^* \bar{y}^{r,t+1} = \frac{1}{\sigma_r} \big( b - A(\bar{x}^{r,t+1} + \sigma_r(\bar{z}^{r,t+1} - c)) \big),
   ```

   which is computationally affordable in practice.  
   In this case, the update rule (2.12) simplifies to

   ```{math}
   \sigma_{r+1} = \frac{\| \bar{x}^{r,\tau_r} - x^{r,0} \|}{\| A^*(\bar{y}^{r,\tau_r} - y^{r,0}) \|}.
   ```

2. **Case $T_1 = \lambda_A I_m - A A^*$ with $\lambda_A \geq \|A\|_2^2$.**  
   Proposed in [13, 4, 42], this choice applies when $l_c \neq u_c$ or when solving (2.13) directly is expensive.  
   The $y$-update takes the form

   ```{math}
   \bar{y}^{r,t+1} = \frac{1}{\sigma_r \lambda_A} \Big( \Pi_{\mathcal{K}}(R_y) - R_y \Big),
   ```

   where $R_y := A(2\bar{x}^{r,t+1} - x^{r,t}) - \sigma_r \lambda_A y^{r,t}$.  
   In this setting, the update for $\sigma$ becomes

   ```{math}
   \sigma_{r+1} = \frac{\| \bar{x}^{r,\tau_r} - x^{r,0} \|}{\sqrt{\lambda_A} \; \| \bar{y}^{r,\tau_r} - y^{r,0} \|}.
   ```

**Remark 2.7.** The update formula above is closely related to the primal weight update in PDLP [1, Algorithm 3], differing mainly by the presence of the factor $\lambda_A$.  

It is worth noting that the approximations $\Delta_x$ and $\Delta_y$ may deviate significantly from the true quantities.  
To address this, various smoothing schemes [1, 31, 33, 6] and safeguards [5] have been proposed to stabilize the update.  
Moreover, the rule (2.12) is not specific to LP; it extends directly to the HPR method for more general convex optimization problems [40], including CCQP [6].
