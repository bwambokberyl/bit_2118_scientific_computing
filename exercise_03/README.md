# Exercise 03: Floating-Point Arithmetic and Numerical Errors

## 1. Concept Overview

Computers represent most real numbers using finite binary precision. Consequently, some decimal values cannot be represented exactly, introducing small numerical errors.

### Essential concepts

**Absolute error:**

$$
E_a = |x_{\text{true}} - x_{\text{approx}}|
$$

**Relative error:**

$$
E_r = \frac{E_a}{|x_{\text{true}}|}
$$

**Percentage relative error:**

$$
E_p = E_r \times 100\%
$$
- **Round-off error:** Occurs when numbers are represented with limited precision.
- **Truncation error:** Occurs when an exact mathematical process is replaced by an approximation.

Floating-point comparisons should use a suitable tolerance rather than relying on exact equality.

NumPy provides `np.isclose()` and `np.allclose()` for tolerance-based comparisons.

## 2. Example

Consider the calculation:

```python
import numpy as np

calculated = 0.1 + 0.2
expected = 0.3

print(calculated == expected)
print(np.isclose(calculated, expected))
```

**Expected output:**

```text
False
True
```

The difference occurs because decimal values such as 0.1 and 0.2 cannot always be represented exactly in binary floating-point arithmetic.

## 3. Applications

1. Structural engineering: Measuring small deformations and material displacement.
2. Scientific simulations: Maintaining numerical accuracy during repeated calculations.
3. GPS and navigation: Processing coordinates and positional measurements.
4. Financial computing: Managing precision in numerical calculations.
5. Numerical modelling: Preventing accumulated errors in iterative algorithms.

## 4. Problem Statement & Dataset

### Problem

A structural engineering monitoring system measures extremely small deformation changes in a bridge.

The engineering team needs to evaluate a mathematical expression involving small numerical values.

Develop a Python program that:

1. Demonstrates floating-point comparison using exact equality and `np.isclose()`.
2. Calculates absolute and relative errors using a reference value of \(\sqrt{5}\) and an approximation of 2.236.
3. Evaluates the following expression using different small values of \(x\):

$$
f(x) = \frac{\sqrt{1+x}-1}{x}
$$

4. Implements an algebraically equivalent, numerically stable expression:

$$
f(x) = \frac{1}{\sqrt{1+x}+1}
$$

5. Compares the results of both expressions.
6. Calculates the numerical difference between the two formulations.

### Dataset

The deformation-related input values are:

```python
x_values = np.array([1e-4, 1e-8, 1e-12])
```

These small values help demonstrate how floating-point precision affects numerical calculations.

### output
[output image](https://github.com/bwambokberyl/bit_2118_scientific_computing/blob/main/output_images/exercise3_output.png)


