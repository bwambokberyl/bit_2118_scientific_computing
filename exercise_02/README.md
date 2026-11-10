# Exercise 02: Mathematical Functions and Vectorization

## 1. Concept Overview

Vectorization is the process of applying mathematical operations to multiple numerical values simultaneously using NumPy arrays.

Instead of processing individual elements using Python loops, NumPy applies mathematical functions to entire arrays.

**Essential mathematical identity:**


$\sin^2(x) + \cos^2(x) = 1$

For an array of angles \(x\), NumPy evaluates:

```python
result = np.sin(x)**2 + np.cos(x)**2
```

Vectorization simplifies numerical computations and can significantly improve execution speed when working with large datasets.

## 2. Example

Calculate the sine of three angles:

```python
import numpy as np

angles = np.array([0, np.pi / 2, np.pi])

result = np.sin(angles)

print(np.round(result, 4))
```

**Expected output:**

```text
[0. 1. 0.]
```

The same operation can be applied to arrays containing millions of values.

## 3. Applications

1. Robotics: Processing joint angles and sensor measurements.
2. Signal processing: Applying mathematical transformations to signals.
3. Image processing: Performing pixel-level mathematical operations.
4. Numerical simulations: Evaluating mathematical models across large datasets.
5. Machine learning: Performing calculations on large feature matrices.

## 4. Problem Statement & Dataset

### Problem

A robotic arm monitoring system records one million angular measurements from its joints during operation.

The engineering team needs to evaluate the trigonometric identity:

$y_i = \sin^2(x_i) + \cos^2(x_i)$


Develop a Python program that:

1. Generates one million angular measurements between 0 and \(2\pi\) radians.
2. Computes the trigonometric expression using a conventional Python loop.
3. Computes the same expression using vectorized NumPy operations.
4. Measures and compares the execution times of both implementations.
5. Calculates the approximate speed-up achieved through vectorization.
6. Verifies that the computed results are approximately equal to 1.

### Dataset

The dataset consists of one million evenly distributed angular measurements:

```python
angles = np.linspace(0, 2 * np.pi, 1_000_000)
```

The dataset is generated programmatically using NumPy.

### Expected Results

- Number of measurements: 1,000,000.
- First five vectorized results: approximately `[1. 1. 1. 1. 1.]`.
- Maximum absolute error from the theoretical value of 1: close to machine precision.
- Vectorized execution should generally be faster than the Python loop.

**Note:** Execution times and speed-up depend on the computer's hardware and current system load.

