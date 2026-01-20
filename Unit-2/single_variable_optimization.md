# Comprehensive Study Guide: Single-Variable Optimization

## 1. Introduction

**Optimization** is the scientific process of determining the best possible solution to a problem given a set of constraints. In engineering and applied sciences, this generally means finding the variables that minimize a cost function or maximize a performance metric.

**Single-Variable Optimization** (also known as One-Dimensional Minimization) is the foundational building block of this discipline. It concerns finding the scalar value $x^*$ that minimizes an objective function $f(x)$.

While many real-world problems involve multiple design variables, single-variable techniques are critical for two reasons:
1.  Many engineering problems naturally depend on a single parameter (e.g., finding the optimal thickness of an insulation layer).
2.  Complex multivariable optimization algorithms often rely on a sequence of single-variable searches (line searches) to determine how far to move in a specific direction.

---

## 2. Analytical Methods (Classical Calculus)

Before employing numerical methods (iterative search algorithms), one must understand the classical analytical approach based on differential calculus. These methods provide the theoretical basis for identifying optimality.

### 2.1 Necessary and Sufficient Conditions

For a continuous and differentiable function $f(x)$, we identify optima by analyzing derivatives.

*   **Stationary Point:** A point $x^*$ where the slope of the function is zero ($f'(x^*) = 0$). This point can be a minimum, a maximum, or an inflection point.

**Theorem: The Necessary Condition**
If a function $f(x)$ has a relative minimum or maximum at $x^*$, and the derivative $f'(x^*)$ exists, then:
$$f'(x^*) = 0$$

**Theorem: The Sufficient Condition**
To distinguish between a minimum and a maximum, we examine the second derivative (curvature) at the stationary point. Let $f'(x^*) = 0$.
*   If $f''(x^*) > 0$: The function is convex (shaped like a bowl). $x^*$ is a **Relative Minimum**.
*   If $f''(x^*) < 0$: The function is concave (shaped like an inverted bowl). $x^*$ is a **Relative Maximum**.
*   If $f''(x^*) = 0$: The test is inconclusive; higher-order derivatives must be examined.

> **![Illustration](images/image_point-7_0.png)**

### 2.2 Example: Manufacturing Optimization
Consider a container manufacturing problem where the cost $C$ depends on the radius $r$ of the cylinder:
$$C(r) = 12\pi r^2 + \frac{2000}{r}$$
To find the optimal radius:
1.  **Differentiate:** $C'(r) = 24\pi r - 2000r^{-2}$.
2.  **Set to zero:** $24\pi r = \frac{2000}{r^2} \Rightarrow r^3 = \frac{2000}{24\pi} \Rightarrow r \approx 2.98$.
3.  **Check sufficiency:** $C''(r) = 24\pi + 4000r^{-3}$. Since $r$ must be positive, $C''(r) > 0$. The cost is minimized.

---

## 3. Numerical Methods: Concepts and Classification

In many engineering scenarios, the objective function $f(x)$ is too complex to differentiate, possesses discontinuities, or is a "black box" simulation where no explicit formula exists. In these cases, we use numerical methods.

### 3.1 Unimodality
The most important concept in numerical search is **Unimodality**. A function is unimodal in an interval $[a, b]$ if it has only one peak (maximum) or one valley (minimum) in that range.

*   **Unimodal Assumption:** Most one-dimensional search algorithms assume the function is unimodal. If a function has multiple local minima (multimodal), these methods guarantee finding *a* local minimum, but not necessarily the *global* minimum.

> **![Illustration](images/image_point-7_1.png)**

### 3.2 Interval of Uncertainty (IoU)
Numerical methods work by iteratively narrowing the range of values where the optimum lies.
*   We start with a wide interval $[a, b]$.
*   We evaluate the function at test points.
*   Based on the results, we discard a portion of the interval.
*   The remaining range is the **Interval of Uncertainty**. The goal is to reduce this interval until it is smaller than a specified tolerance.

---

## 4. Elimination Methods

Elimination methods focus on narrowing the search interval by comparing function values at specific test points. They do not require calculation of derivatives.

### 4.1 Unrestricted Search
This is a crude method used when the initial bounds $[a, b]$ are unknown.
1.  Start at a point $x_1$ with a step size $s$.
2.  Evaluate $f(x_1)$ and $f(x_1 + s)$.
3.  If the function value decreases, keep stepping forward.
4.  If the function value increases, the minimum has been passed; the search terminates or reverses with a smaller step.

### 4.2 Exhaustive Search
This method divides the interval $[a, b]$ into $n$ equally spaced points.
*   We evaluate the function at all $n$ points.
*   We select the point with the lowest function value.
*   **Pros:** Reliable.
*   **Cons:** Very inefficient. Requires a massive number of function evaluations to achieve high accuracy.

### 4.3 Dichotomous Search
In this method, two experiments are placed very close to the center of the interval.
1.  Interval: $[L, R]$. Midpoint $M = (L+R)/2$.
2.  Test points: $x_1 = M - \epsilon$ and $x_2 = M + \epsilon$ (where $\epsilon$ is a small number).
3.  If $f(x_1) < f(x_2)$, the minimum lies to the left of $M$. Eliminate the region $[x_2, R]$.
4.  If $f(x_1) > f(x_2)$, the minimum lies to the right of $M$. Eliminate the region $[L, x_1]$.
*   **Efficiency:** Each iteration almost halves the interval.

### 4.4 Golden Section Method
This is one of the most popular and elegant elimination methods. It is efficient because it reduces the interval by a constant ratio at every step while reusing one previous function evaluation.

**The Golden Ratio ($\phi$):**
The interval is divided based on the golden ratio, approximately $0.618$.
$$ \tau = \frac{\sqrt{5} - 1}{2} \approx 0.618 $$

**The Algorithm:**
Given an interval of uncertainty $L_0$:
1.  Place two points at distance $0.618 L_0$ from either end.
2.  Evaluate $f(x_1)$ and $f(x_2)$.
3.  Discard the section closest to the higher function value (for minimization).
4.  **Crucial Feature:** In the remaining interval, one of the old test points sits exactly at the "golden section" spot of the new interval. Only **one** new function evaluation is needed per iteration.

**Real-World Application:**
Imagine tuning a radio receiver circuit to minimize noise. The frequency range is 88–108 MHz. Instead of turning the dial linearly, the Golden Section method suggests specific frequencies to test, rapidly isolating the point of minimum noise with very few adjustments.

> **![Illustration](images/image_point-7_2.png) with points x1 at 0.382 and x2 at 0.618. Step 2 shows the interval shrinking, demonstrating that the old x1 becomes the new x2 (or vice versa), requiring only one new point calculation.]**

### 4.5 Fibonacci Method
This method is similar to the Golden Section search but is based on the Fibonacci sequence $(1, 1, 2, 3, 5, 8, 13...)$.
*   It is theoretically the most efficient elimination method if the number of available function evaluations ($n$) is fixed and known in advance.
*   The interval reduction ratio changes slightly at each step, converging toward 0.618 as $n$ approaches infinity.

---

## 5. Interpolation Methods

Elimination methods only use the *relative order* of function values (is A < B?). They ignore the *magnitude* of the difference. Interpolation methods use the magnitudes to fit a polynomial curve to the test points and estimate the minimum of that curve.

### 5.1 Quadratic Interpolation
If a function is smooth and continuous near the minimum, it can be approximated by a parabola (quadratic equation) $q(x) = ax^2 + bx + c$.

**Procedure:**
1.  Evaluate the function at three points: $A, B, C$.
2.  Fit a parabola through these three points.
3.  Analytically calculate the minimum of this parabola.
4.  Use this predicted minimum as a new test point.
5.  Discard the "worst" of the four points and repeat.

*   **Advantage:** Converges much faster than elimination methods for smooth functions.
*   **Disadvantage:** Can be unstable if the three points fall in a straight line or if the function is highly irregular.

### 5.2 Cubic Interpolation
This method fits a third-degree polynomial (cubic) to the data. It generally requires knowing both the function values $f(x)$ and the derivatives $f'(x)$ at two points. It is commonly used when gradient information is available.

---

## 6. Direct Root Methods (Gradient-Based)

If the derivative of the function is available, we can find the minimum by solving the root-finding problem $f'(x) = 0$.

### 6.1 Newton's Method (Newton-Raphson)
This method uses a second-order Taylor series approximation. It assumes the function is quadratic near the optimum.

**Formula:**
$$ x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)} $$

*   **Process:**
    1.  Start at guess $x_k$.
    2.  Calculate the first derivative (slope) and second derivative (curvature).
    3.  Project a tangent curve to find where the derivative would equal zero.
*   **Convergence:** Quadratic convergence (extremely fast) if started near the optimum.
*   **Limitations:** Requires calculation of first and second derivatives. If $f''(x) = 0$ or is negative, the method may diverge or find a maximum instead of a minimum.

### 6.2 Quasi-Newton (Secant) Method
This is a modification of Newton's method for cases where the second derivative $f''(x)$ is difficult to calculate. It approximates the second derivative using finite differences of the first derivative.

**Formula:**
It replaces $f''(x)$ with the slope of the secant line between two previous derivative values:
$$ f''(x) \approx \frac{f'(x_k) - f'(x_{k-1})}{x_k - x_{k-1}} $$

This combines the speed of Newton's method with the simplicity of not requiring analytical second derivatives.

---

## 7. Comparison of Methods Table

| Method Category | Specific Method | Best Used When... | Requirements | Convergence Speed |
| :--- | :--- | :--- | :--- | :--- |
| **Elimination** | Unrestricted Search | Bounds are unknown | Function values | Slow |
| **Elimination** | Golden Section | Robustness is required; function is unimodal but non-smooth | Function values | Moderate (Linear) |
| **Interpolation** | Quadratic | Function is smooth and continuous | Function values | Fast (Superlinear) |
| **Root Finding** | Newton's Method | Derivatives are easy to calculate; starting point is good | $f'(x)$ and $f''(x)$ | Very Fast (Quadratic) |
| **Root Finding** | Secant Method | $f''(x)$ is hard to compute | $f'(x)$ | Fast |

---

## 8. Practical Considerations

In engineering optimization (e.g., MATLAB implementation), we often combine methods. A robust algorithm might start with a **Golden Section search** to bracket the minimum reliably and reduce the interval of uncertainty. Once the interval is small and the function behaves smoothly, the algorithm switches to **Inverse Quadratic Interpolation** or **Newton's Method** to snap quickly to the precise optimal value.

### Key Takeaways for Students:
1.  **Stationary Points:** Finding where slope = 0 is the core of analytical optimization.
2.  **Unimodality:** Numerical methods rely on the assumption that there is only one valley to find.
3.  **Trade-off:** There is always a trade-off between the number of function evaluations (cost) and the accuracy of the result.
4.  **Derivative Availability:** If you have derivatives, use them (Newton/Secant). If not, use Elimination methods (Golden Section).