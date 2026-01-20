Here is a comprehensive study guide section based on the provided textbook content, specifically expanded from **Chapter 2: Classical Optimization Techniques**, focusing on Section 2.5 and related concepts.

---

# Study Guide: Multivariable Optimization with Inequality Constraints

## 1. Introduction
In real-world engineering and economic systems, design variables are rarely free to take on any value. They are restricted by physical limitations such as material yield strength, budgetary caps, maximum deflection limits, or available labor hours. While equality constraints ($h(x) = 0$) define precise relationships, **inequality constraints** ($g(x) \le 0$) define boundaries within which a solution must lie.

This section explores the mathematical framework for solving optimization problems where the restrictions are defined by inequalities. Unlike equality constraints, which force the solution to lie *on* a curve or surface, inequality constraints allow the solution to lie *on* the boundary or *inside* the feasible region.

### The General Problem Statement
The standard mathematical formulation for a minimization problem with inequality constraints is:

**Find** $X = \{x_1, x_2, ... x_n\}^T$  
**To Minimize:** $f(X)$  
**Subject to:**  
$$g_j(X) \le 0, \quad j = 1, 2, ..., m$$

> **Note on Maximization:** If the problem requires maximization, it can be converted to minimization by negating the objective function: $\text{Maximize } f(X) \equiv \text{Minimize } -f(X)$. Similarly, a constraint of the form $G_j(X) \ge 0$ can be multiplied by $-1$ to fit the standard form: $-G_j(X) \le 0$.

---

## 2. Fundamental Concepts

### 2.1 The Feasible Region
The inequality constraints define a region in the design space known as the **feasible region**.
*   **Feasible Points:** Points where all $g_j(X) \le 0$.
*   **Infeasible Points:** Points where at least one $g_j(X) > 0$.

### 2.2 Active vs. Inactive Constraints
A crucial concept in solving these problems is determining whether a constraint "matters" at the optimal solution point $X^*$.

1.  **Active Constraint:** A constraint is active if, at the optimum, the design point lies exactly on the boundary limit. Mathematically, $g_j(X^*) = 0$. The constraint essentially acts as an equality constraint at this point, restricting movement in certain directions.
2.  **Inactive Constraint:** A constraint is inactive if the optimum point lies strictly inside the boundary. Mathematically, $g_j(X^*) < 0$. If a constraint is inactive, small changes in the design variables near the optimum do not trigger this restriction; the system behaves locally as if this constraint did not exist.

> **![Illustration](images/image_point-12_0.png)**

---

## 3. Transformation to Equality Constraints
Classical calculus methods (like Lagrange Multipliers) are designed for equality constraints. To utilize these tools for inequalities, we must mathematically transform the inequalities into equalities.

### 3.1 Slack Variables
We introduce **slack variables** to take up the "slack" between the function value and zero. Because the constraint is $g_j(X) \le 0$, we must add a non-negative value to reach zero.

To ensure the slack variable is non-negative, it is often defined as a squared term, $y_j^2$.
$$g_j(X) + y_j^2 = 0$$
Where $y_j$ is an unknown real number.

*   If $y_j = 0$, then $g_j(X) = 0$ (The constraint is **Active**).
*   If $y_j \neq 0$, then $y_j^2 > 0$, implying $g_j(X) < 0$ (The constraint is **Inactive**).

### 3.2 The Modified Lagrange Function
We construct the Lagrange function $L$ by incorporating the objective function and the transformed constraints using Lagrange multipliers ($\lambda_j$):

$$L(X, Y, \lambda) = f(X) + \sum_{j=1}^{m} \lambda_j [g_j(X) + y_j^2]$$

Here, the unknowns are the design variables ($X$), the slack variables ($Y$), and the Lagrange multipliers ($\lambda$).

---

## 4. The Kuhn-Tucker (K-T) Conditions
The most significant development in nonlinear programming with inequality constraints was provided by Kuhn and Tucker (1951). They derived the necessary conditions for a point $X^*$ to be a relative minimum.

To find the stationary point of the Lagrange function derived in Section 3.2, we take partial derivatives with respect to all variables ($x_i, y_j, \lambda_j$) and set them to zero. This yields the famous **Kuhn-Tucker Conditions**.

### 4.1 The Necessary Conditions
For a point $X^*$ to be a local minimum, the following conditions must hold:

| Condition Name | Mathematical Expression | Interpretation |
| :--- | :--- | :--- |
| **1. Gradient Condition** | $\frac{\partial f}{\partial x_i} + \sum_{j=1}^{m} \lambda_j \frac{\partial g_j}{\partial x_i} = 0$ | The negative gradient of the objective function ($-\nabla f$) must be a linear combination of the gradients of the active constraints. |
| **2. Primal Feasibility** | $g_j(X) \le 0$ | The solution must not violate any constraints. |
| **3. Complementary Slackness** | $\lambda_j y_j = 0 \implies \lambda_j g_j(X) = 0$ | This is the "switching" condition. Either the constraint is active ($g_j=0$) or the multiplier is zero ($\lambda_j=0$). |
| **4. Dual Feasibility** | $\lambda_j \ge 0$ | The Lagrange multipliers must be non-negative for minimization problems with "$\le$" constraints. |

> **![Illustration](images/image_point-12_1.png)**

### 4.2 Understanding Complementary Slackness
The condition $\lambda_j g_j(X) = 0$ is critical for solving these problems. It creates two distinct cases for every constraint:

*   **Case A:** $\lambda_j > 0$. This implies $g_j(X)$ **must** be 0. The constraint is **Active**. The limit is preventing the objective function from reaching a lower value (the constraint is "binding").
*   **Case B:** $\lambda_j = 0$. This implies $g_j(X)$ can be $< 0$. The constraint is **Inactive**. The boundary is not currently influencing the local optimum.

### 4.3 Interpretation of the Multiplier ($\lambda$)
In engineering and economics, the Lagrange multiplier $\lambda$ is often called the **Shadow Price** or **Sensitivity Coefficient**.
*   It represents the change in the optimal objective function value $f^*$ per unit change in the constraint limit.
*   If $\lambda_j$ is large, tightening that constraint slightly will cause a large increase in the cost (or objective).
*   If $\lambda_j = 0$, relaxing or tightening that constraint slightly will have no immediate effect on the optimum design.

---

## 5. Constraint Qualification and Convexity

### 5.1 Constraint Qualification
For the Kuhn-Tucker conditions to be valid, a condition known as **Constraint Qualification** must be met at the optimum point. Generally, this requires that the gradients of the active constraints ($\nabla g_j$) at the optimum point must be **linearly independent**.

If the gradients are dependent (e.g., two constraints form a "cusp" pointing in the same direction), the standard K-T conditions might fail to identify the minimum. However, in most engineering applications with linear or convex constraints, this qualification is usually satisfied.

### 5.2 Convex Programming
While K-T conditions are *necessary* for a relative minimum, they are not always *sufficient* (they might identify a maximum or a saddle point). However, for a specific class of problems called **Convex Programming Problems**, the K-T conditions are both necessary and **sufficient** for a **global** minimum.

A problem is a Convex Programming problem if:
1.  The objective function $f(X)$ is convex.
2.  The inequality constraints $g_j(X)$ are convex functions.
3.  The equality constraints (if any) are linear.

---

## 6. Computational Procedure: How to Solve
When solving a problem analytically using K-T conditions, you generally do not know which constraints are active beforehand. Therefore, a trial-and-error approach is often required.

**Step 1: Formulate the Lagrangian**
Write out $L = f(X) + \sum \lambda_j g_j(X)$.

**Step 2: Generate the K-T Equations**
1.  $\nabla f + \sum \lambda \nabla g = 0$ (Stationarity)
2.  $g_j(X) \le 0$ (Feasibility)
3.  $\lambda_j g_j(X) = 0$ (Complementary Slackness)
4.  $\lambda_j \ge 0$ (Non-negativity)

**Step 3: Test Hypotheses (Cases)**
Since each constraint can be either active ($\lambda > 0, g=0$) or inactive ($\lambda = 0, g < 0$), for a problem with $m$ constraints, there are potentially $2^m$ combinations to test.

*   **Trial 1:** Assume no constraints are active (all $\lambda = 0$). Solve $\nabla f = 0$. Check if the resulting $X$ satisfies all $g_j(X) \le 0$. If yes, you are done.
*   **Trial 2:** Assume one constraint is active (e.g., $\lambda_1 > 0, g_1 = 0$). Solve the system. Check if $\lambda_1$ comes out positive and if other constraints are satisfied.
*   **Trial 3:** Assume multiple constraints are active.

**Step 4: Verify**
The valid solution must satisfy the stationarity equations, primal feasibility, and result in positive $\lambda$ values for all active constraints.

---

## 7. Detailed Example: Optimal Design

### Problem Statement
Minimize $f(x_1, x_2) = (x_1 - 1)^2 + x_2^2 - 2$
Subject to:
1.  $2x_1 + x_2 \le 6$
2.  $x_1 - 4x_2 \le 0$
3.  $x_1 \ge 0, x_2 \ge 0$ (Side constraints)

### Solution Walkthrough

**1. Standard Form:**
Maximize constraints must be converted to $\le 0$.
$g_1(X) = 2x_1 + x_2 - 6 \le 0$
$g_2(X) = x_1 - 4x_2 \le 0$
$g_3(X) = -x_1 \le 0$
$g_4(X) = -x_2 \le 0$

**2. K-T Conditions (Stationarity):**
$\nabla f = \{2(x_1-1), 2x_2\}^T$
$\nabla g_1 = \{2, 1\}^T$
$\nabla g_2 = \{1, -4\}^T$

The gradient equation ($\nabla f + \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2 ... = 0$) gives:
1.  $2(x_1 - 1) + 2\lambda_1 + \lambda_2 - \lambda_3 = 0$
2.  $2x_2 + \lambda_1 - 4\lambda_2 - \lambda_4 = 0$

**3. Investigating Cases:**

*Case A: No constraints active ($\lambda_1 = \lambda_2 = \lambda_3 = \lambda_4 = 0$)*
Equations become:
$2(x_1 - 1) = 0 \rightarrow x_1 = 1$
$2x_2 = 0 \rightarrow x_2 = 0$
Check feasibility of point (1, 0):
$g_2(1,0) = 1 - 0 = 1 \not\le 0$. **Violation.** This constraint must be active.

*Case B: Constraint 2 is active ($\lambda_2 > 0, g_2=0$), others inactive.*
Set $g_2 = x_1 - 4x_2 = 0 \rightarrow x_1 = 4x_2$.
Substitute into stationarity equations (with $\lambda_1, \lambda_3, \lambda_4 = 0$):
1. $2(4x_2 - 1) + \lambda_2 = 0 \rightarrow \lambda_2 = 2 - 8x_2$
2. $2x_2 - 4\lambda_2 = 0 \rightarrow x_2 = 2\lambda_2$

Solving this system:
$x_2 = 2(2 - 8x_2) \rightarrow x_2 = 4 - 16x_2 \rightarrow 17x_2 = 4 \rightarrow x_2 = 4/17$.
Then $x_1 = 16/17$.
Calculate $\lambda_2$: $x_2 = 2\lambda_2 \rightarrow \lambda_2 = x_2/2 = 2/17$.

**Check Validity:**
1.  Is $\lambda_2 > 0$? Yes ($2/17 > 0$).
2.  Are other constraints satisfied?
    *   $g_1: 2(16/17) + (4/17) - 6 = 36/17 - 102/17 < 0$. (Satisfied).
    *   $g_3, g_4$: $x_1, x_2$ are positive. (Satisfied).

**Conclusion:**
The minimum is at $X^* = (16/17, 4/17)$ with active constraint $g_2$. The Lagrange multiplier $\lambda_2 = 2/17$ indicates that relaxing constraint $g_2$ by 1 unit would lower the objective function by approximately $2/17$.

---

## 8. Real-World Applications

### 8.1 Structural Optimization
In civil and mechanical engineering, K-T conditions are used to minimize the weight of a truss or frame.
*   **Objective:** Minimize Weight (function of cross-sectional areas).
*   **Inequality Constraints:** Stress $\sigma \le \sigma_{yield}$, Deflection $\delta \le \delta_{max}$.
*   **Side Constraints:** Area $A \ge 0$.

### 8.2 Manufacturing Economics
*   **Objective:** Minimize Cost or Maximize Profit.
*   **Inequality Constraints:** Machine time available $\le 8$ hours, Raw material usage $\le$ Inventory limits.
*   **Significance of $\lambda$:** The value of $\lambda$ for the "Machine Time" constraint tells the manager exactly how much extra profit they would make if they paid for one hour of overtime.

### 8.3 Control Systems
*   **Objective:** Minimize error over a trajectory.
*   **Inequality Constraints:** The control input (thrust, voltage) cannot exceed physical saturation limits ($|u| \le U_{max}$).

---

> **![Illustration](images/image_point-12_2.png)**