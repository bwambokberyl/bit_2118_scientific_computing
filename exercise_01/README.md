# Exercise 02: NumPy Arrays and Numerical Computation

## 1. Concept Overview

NumPy arrays store numerical data and allow mathematical operations to be performed efficiently across multiple elements.

A vector is a one-dimensional array, while a matrix is a two-dimensional array.

**Essential operations:**

- Mean
- Minimum: `min(x)`
- Maximum `max(x)`
- Unit conversion

NumPy supports vectorized operations, allowing calculations to be applied to entire arrays without manually writing loops.

## 2. Example

Consider particulate matter measurements:

```python
import numpy as np

readings = np.array([2.0, 4.0, 6.0])

print(np.mean(readings))
print(readings / 2)
```

**Expected output:**

```text
4.0
[1. 2. 3.]
```

## 3. Applications

1. Environmental air-quality monitoring.
2. Processing sensor measurements from IoT devices.
3. Image processing and pixel manipulation.
4. Scientific and engineering measurements.
5. Machine-learning datasets.

## 4. Problem Statement & Dataset

### Problem

An environmental monitoring station records hourly concentrations of PM2.5 particulate matter over a 24-hour period.

Develop a Python program that uses NumPy to:

1. Store the 24 measurements in a one-dimensional array.
2. Calculate the daily mean concentration.
3. Identify the minimum and maximum concentrations.
4. Convert all measurements from micrograms per cubic metre (µg/m³) to milligrams per cubic metre (mg/m³).
5. Display the first six converted measurements.

### Dataset

PM2.5 measurements (µg/m³):

```python
[12.4, 11.8, 10.9, 10.2, 11.1, 13.6,
 18.2, 22.5, 26.1, 29.4, 31.0, 28.7,
 27.3, 25.8, 24.6, 23.1, 21.7, 20.4,
 19.2, 18.0, 16.8, 15.5, 14.3, 13.1]
```

### Expected Results

| Measurement | Expected result |
|---|---:|
| Number of readings | 24 |
| Daily mean | 19.40 µg/m³ |
| Minimum | 10.20 µg/m³ |
| Maximum | 31.00 µg/m³ |

First six converted readings:

```text
[0.0124 0.0118 0.0109 0.0102 0.0111 0.0136]
```

## 5. Execution

From the monorepo root:

```bash
python3 exercise_06_numpy_arrays/solution.py
```