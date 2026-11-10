"""
File: exercise_02_mathematical_functions_vectorization/solution.py

Purpose:
Demonstrate mathematical functions and vectorization using NumPy.
Compare loop-based and vectorized trigonometric computations
using one million robotic joint-angle measurements.
"""

import math
import timeit

import numpy as np
import numpy.typing as npt


def generate_data() -> npt.NDArray[np.float64]:
    """Generate one million angular measurements in radians."""
    angles = np.linspace(
        0,
        2 * np.pi,
        1_000_000,
        dtype=np.float64,
    )

    return angles


def loop_version(
    angles: npt.NDArray[np.float64],
) -> list[float]:
    """Calculate the trigonometric expression using a Python loop."""
    results = []

    for angle in angles:
        value = math.sin(angle) ** 2 + math.cos(angle) ** 2
        results.append(value)

    return results


def vectorized_version(
    angles: npt.NDArray[np.float64],
) -> npt.NDArray[np.float64]:
    """Calculate the expression using vectorized NumPy operations."""
    return np.sin(angles) ** 2 + np.cos(angles) ** 2


def benchmark(
    angles: npt.NDArray[np.float64],
) -> tuple[float, float]:
    """Measure execution times for both implementations."""
    loop_time = timeit.timeit(
        lambda: loop_version(angles),
        number=1,
    )

    vector_time = timeit.timeit(
        lambda: vectorized_version(angles),
        number=3,
    ) / 3

    return loop_time, vector_time


def display_results(
    results: npt.NDArray[np.float64],
    loop_time: float,
    vector_time: float,
) -> None:
    """Display computation results and performance comparison."""
    max_error = float(np.max(np.abs(results - 1.0)))

    speedup = loop_time / vector_time if vector_time > 0 else 0.0

    print("ROBOTIC JOINT-ANGLE COMPUTATION")
    print("-" * 40)

    print(f"Number of measurements: {len(results):,}")

    print("\nFirst five computed values:")
    print(np.round(results[:5], 10))

    print("\nNumerical verification:")
    print(f"Mean result: {np.mean(results):.12f}")
    print(f"Maximum absolute error: {max_error:.3e}")
    print(f"All values approximately equal to 1: "
          f"{np.allclose(results, 1.0)}")

    print("\nPerformance comparison:")
    print(f"Python loop time: {loop_time:.4f} seconds")
    print(f"Vectorized time: {vector_time:.4f} seconds")
    print(f"Approximate speed-up: {speedup:.2f}x")


def main() -> None:
    """Execute the vectorization experiment."""
    angles = generate_data()

    loop_time, vector_time = benchmark(angles)

    results = vectorized_version(angles)

    display_results(results, loop_time, vector_time)


if __name__ == "__main__":
    main()
