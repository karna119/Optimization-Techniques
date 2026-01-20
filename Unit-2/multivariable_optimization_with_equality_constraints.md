Based on the textbook *Engineering Optimization: Theory and Practice* by Singiresu S. Rao, specifically **Chapter 2.4: Multivariable Optimization with Equality Constraints**, here is a comprehensive study guide.

---

# Study Guide: Multivariable Optimization with Equality Constraints

## 1. Introduction and Problem Formulation

In engineering design, variables are rarely independent. A design engineer often seeks to minimize a cost or weight function while adhering to strict physical laws or geometric limitations. When these limitations must be met exactly (e.g., "The total flow *must equal* 100 kg/s" or "The beam length *must equal* $L$"), they are classified as **Equality Constraints**.

### The Mathematical Formulation
The general problem of multivariable optimization with equality constraints is defined as:

Find the **Design Vector** $X$:
$$X = \{x_1, x_2, ... x_n\}^T$$

To minimize the **Objective Function**:
$$f(X)$$

Subject to $m$ **Equality Constraints**:
$$g_j(X) = 0, \quad j = 1, 2, ..., m$$

**Key Constraints on the Problem Structure:**
*   **$n$ (Variables) > $m$ (Constraints):** The number of variables must exceed the number of equality constraints.
    *   If $n = m$: The problem is determined (provided the equations are independent). There is likely only one unique solution for $X$, leaving no room for optimization.
    *   If $n < m$: The problem is over-determined and generally has no solution.
*   The difference $n - m$ represents the **degrees of freedom** of the system.

---

## 2. Method 1: Direct Substitution

The simplest conceptual approach to solving constrained problems is to convert them into unconstrained problems. This is done by using the constraint equations to eliminate variables.

### The Procedure
1.  Given $m$ constraint equations, solve them simultaneously to express $m$ variables in terms of the remaining $n - m$ variables.
2.  Substitute these expressions into the original objective function $f(X)$.
3.  The result is a new objective function involving only $n - m$ variables with *no* constraints.
4.  Solve using standard unconstrained optimization techniques (setting partial derivatives to zero).

### Real-World Example: Box Inscribed in a Sphere
Consider designing a rectangular box of maximum volume inside a sphere of unit radius.
*   **Variables:** $x_1, x_2, x_3$ (dimensions of the box).
*   **Objective:** Maximize Volume $f = 8x_1x_2x_3$.
*   **Constraint:** The corners must touch the sphere surface: $x_1^2 + x_2^2 + x_3^2 = 1$.

Using direct substitution, we can solve the constraint for $x_3$:
$$x_3 = \sqrt{1 - x_1^2 - x_2^2}$$

Substitute this into the objective function:
$$f(x_1, x_2) = 8x_1x_2\sqrt{1 - x_1^2 - x_2^2}$$

Now, the problem is reduced to finding the maximum of a two-variable unconstrained function.

### Limitations
While theoretically sound, Direct Substitution is often impractical in complex engineering problems because:
1.  Constraint equations are often highly nonlinear, making it mathematically impossible to explicitly solve for one variable in terms of others.
2.  The resulting unconstrained objective function often becomes unwieldy and difficult to differentiate.

---

## 3. Method 2: The Method of Constrained Variation

This method focuses on the calculus of differential variations. It seeks to find a closed-form expression for the first-order differential of the objective function ($df$) at points where the constraints are satisfied.

### The Concept of Admissible Variations
For a point $X^*$ to be a minimum, the total derivative of the objective function must be zero ($df = 0$). However, we cannot vary all $x_i$ independently. We are restricted to **Admissible Variations**.

An admissible variation is a small movement ($dx$) away from a point $X^*$ such that we remain *on* the constraint surface. If we move off the constraint surface, the variation is inadmissible.

Mathematically, if $g(x_1, x_2) = 0$, then any variation $dx_1, dx_2$ must satisfy:
$$dg = \frac{\partial g}{\partial x_1}dx_1 + \frac{\partial g}{\partial x_2}dx_2 = 0$$

### [IMAGE PLACEHOLDER]
*[Description: A diagram showing a 2D design space with a curved line representing the constraint g(x)=0. A point A lies on the curve. Arrows emanating from A along the curve represent "Admissible Variations" (dx). Arrows pointing away from the curve into the infeasible region represent inadmissible variations. This illustrates that search directions are limited to the tangent of the constraint surface.]*

### The General Necessary Condition
Using the Jacobian determinant, the necessary condition for a constrained optimum at $X^*$ is:

$$J \left( \frac{f, g_1, g_2, ... g_m}{x_k, x_1, x_2, ... x_m} \right) = 0$$

Where $k$ takes values from $m+1$ to $n$. This determinant method essentially checks for linear dependence between the gradients of the objective function and the constraints. While valid, evaluating determinants of order $m+1$ is computationally heavy, leading to the preference for the Lagrange Multiplier method.

---

## 4. Method 3: The Method of Lagrange Multipliers

This is the most powerful and commonly used classical technique for equality constraints. It introduces auxiliary variables (multipliers) to penalize the violation of constraints, effectively coupling the constraints to the objective function.

### 4.1 Definition of the Lagrange Function
We construct a new function, $L$, called the **Lagrange Function** (or Lagrangian):

$$L(x_1, ..., x_n, \lambda_1, ..., \lambda_m) = f(X) + \sum_{j=1}^{m} \lambda_j g_j(X)$$

Here, $\lambda_j$ are unknown constants called **Lagrange Multipliers**. There is one multiplier for each constraint.

### 4.2 Necessary Conditions for Optimality
By treating $L$ as a function of $n + m$ variables ($x$ variables plus $\lambda$ variables), we look for the stationary point where partial derivatives with respect to *all* variables are zero.

This yields a system of equations:
1.  **With respect to design variables:**
    $$\frac{\partial L}{\partial x_i} = \frac{\partial f}{\partial x_i} + \sum_{j=1}^{m} \lambda_j \frac{\partial g_j}{\partial x_i} = 0, \quad i = 1, ..., n$$
2.  **With respect to multipliers (returns the constraints):**
    $$\frac{\partial L}{\partial \lambda_j} = g_j(X) = 0, \quad j = 1, ..., m$$

This results in a system of $n + m$ (often nonlinear) simultaneous equations to solve for $X^*$ and $\lambda^*$.

### 4.3 Geometric Interpretation
The necessary condition implies that at the optimum point, the gradient of the objective function, $\nabla f$, is a linear combination of the gradients of the constraints, $\nabla g_j$.

$$-\nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2 + ...$$

Geometrically, this means the contour of the objective function is **tangent** to the constraint surface at the optimum point. If they were not tangent, the objective contour would cross the constraint, implying you could move further along the constraint to improve the objective function.

### [IMAGE PLACEHOLDER]
*[Description: A contour plot. Curved lines represent contours of f(x) (e.g., elevation lines). A bold line represents the constraint g(x)=0. At the optimum point, the constraint line touches an objective contour tangentially. Vectors representing the gradient of f and the gradient of g are shown originating from this tangent point; they are collinear (parallel), illustrating that one is a scalar multiple ($\lambda$) of the other.]*

### 4.4 Physical Meaning of Lagrange Multipliers ($\lambda$)
In engineering and economics, the Lagrange multiplier $\lambda^*$ is not just a mathematical artifact; it carries significant physical meaning known as **Sensitivity Analysis** or **Shadow Prices**.

If the constraint is changed from $g_j(X) = 0$ to $g_j(X) = b$ (relaxing or tightening the resource availability), the rate of change of the optimal objective function $f^*$ with respect to this change $b$ is:

$$\frac{d f^*}{db} = \lambda^*$$

*   **Interpretation:** $\lambda^*$ tells the designer how much the optimal cost/weight/performance will improve if a specific constraint is relaxed by one unit.
*   **High $\lambda$:** The constraint is a "bottleneck." Relaxing it yields massive gains.
*   **$\lambda = 0$:** The constraint is not binding or changing it does not affect the optimal cost locally.

### 4.5 Sufficient Conditions (The Hessian)
Finding the stationary point of $L$ gives us candidates for the optimum. To determine if a candidate is a minimum, maximum, or saddle point, we must examine the second derivatives.

For functions with constraints, we check the **Bordered Hessian Matrix** (a matrix of second derivatives of $L$ "bordered" by first derivatives of $g$).

*   **Condition:** The quadratic form $Q$ defined by second derivatives must be **positive definite** for a minimum (or negative definite for a maximum) for all variations $dX$ that satisfy the constraints.

---

## 5. Engineering Application Example: Optimal Cylinder Design

**Problem:** Design a cylindrical tin can (with a top and bottom) to maximize volume, subject to a fixed limit on the total surface area of sheet metal available, $A_0 = 24\pi$.

**Variables:**
*   $x_1$: Radius ($r$)
*   $x_2$: Height ($h$)

**Objective Function (Maximize Volume):**
$$f(x_1, x_2) = \pi x_1^2 x_2$$

**Constraint (Surface Area):**
$$g(x_1, x_2) = 2\pi x_1^2 + 2\pi x_1 x_2 - 24\pi = 0$$

### Step 1: Construct the Lagrangian
$$L = \pi x_1^2 x_2 + \lambda(2\pi x_1^2 + 2\pi x_1 x_2 - 24\pi)$$

### Step 2: Apply Necessary Conditions
Differentiate $L$ with respect to $x_1, x_2,$ and $\lambda$:

1.  $\frac{\partial L}{\partial x_1} = 2\pi x_1 x_2 + \lambda(4\pi x_1 + 2\pi x_2) = 0$
2.  $\frac{\partial L}{\partial x_2} = \pi x_1^2 + \lambda(2\pi x_1) = 0$
3.  $\frac{\partial L}{\partial \lambda} = 2\pi x_1^2 + 2\pi x_1 x_2 - 24\pi = 0$

### Step 3: Solve the System
From equation (2), assuming $x_1 \neq 0$:
$$\lambda = -\frac{x_1}{2}$$

Substitute $\lambda$ into equation (1):
$$2\pi x_1 x_2 - \frac{x_1}{2}(4\pi x_1 + 2\pi x_2) = 0$$
$$2\pi x_1 x_2 - 2\pi x_1^2 - \pi x_1 x_2 = 0$$
$$\pi x_1 x_2 - 2\pi x_1^2 = 0$$

Dividing by $\pi x_1$:
$$x_2 = 2x_1$$
*(This is a classic result: The optimal cylinder height equals its diameter).*

Substitute $x_2 = 2x_1$ into the constraint (equation 3):
$$2\pi x_1^2 + 2\pi x_1(2x_1) = 24\pi$$
$$6\pi x_1^2 = 24\pi$$
$$x_1^2 = 4 \implies x_1 = 2$$

Since $x_2 = 2x_1$, then $x_2 = 4$.

**Optimal Design:** Radius = 2, Height = 4.

---

## 6. Summary Table: Comparison of Techniques

| Technique | Description | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **Direct Substitution** | Solve constraints for variables and substitute into objective. | Conceptually simple; reduces dimensionality. | Hard/impossible for complex nonlinear constraints; algebra can become messy. |
| **Constrained Variation** | Uses Jacobian determinants to ensure variations track the constraint surface. | Provides geometric insight into admissible movements. | Evaluating large determinants is computationally inefficient and complex. |
| **Lagrange Multipliers** | Introduces auxiliary variables to create an unconstrained Lagrangian function. | Handles nonlinear constraints well; $\lambda$ provides sensitivity data (shadow prices). | Increases the number of unknowns ($n + m$ variables); requires solving simultaneous nonlinear equations. |

## 7. Key Definitions

*   **Active Constraint:** A constraint that holds as a strict equality ($g(X)=0$) at the optimum point. In equality constrained problems, all constraints are effectively active.
*   **Design Space:** The n-dimensional Cartesian space defined by the design variables.
*   **Constraint Surface:** The subspace (hypersurface) within the design space where the constraint equations are satisfied.
*   **Stationary Point:** A point where the gradient of the function is zero; a candidate for a minimum or maximum.
*   **Shadow Price:** The change in the optimal objective value per unit change in the constraint resource/limit (represented by $\lambda$).