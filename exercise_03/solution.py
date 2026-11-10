"""
File: exercise_03/solution.py

Purpose:
Demonstrate floating-point arithmetic, numerical errors,
and numerical stability using NumPy.

Application:
Precision analysis in structural engineering measurements.
"""

import numpy as np
import numpy.typing as npt


def demonstrate_float_comparison() -> None:
    """Demonstrate floating-point comparison using tolerance."""
    calculated = 0.1 + 0.2
    expected = 0.3

    print("FLOATING-POINT COMPARISON")
    print("-" * 40)

    print(f"Calculated value: {calculated:.17f}")
    print(f"Expected value:   {expected:.17f}")
    print(f"Exact comparison: {calculated == expected}")
    print(f"Tolerance comparison: {np.isclose(calculated, expected)}")


def calculate_errors() -> tuple[float, float, float]:
    """Calculate absolute, relative, and percentage errors."""
    true_value = float(np.sqrt(5))
    approximate_value = 2.236

    absolute_error = abs(true_value - approximate_value)
    relative_error = absolute_error / abs(true_value)
    percentage_error = relative_error * 100

    return absolute_error, relative_error, percentage_error


def calculate_direct(
    x_values: npt.NDArray[np.float64],
) -> npt.NDArray[np.float64]:
    """Evaluate the original mathematical expression."""
    return (np.sqrt(1 + x_values) - 1) / x_values


def calculate_stable(
    x_values: npt.NDArray[np.float64],
) -> npt.NDArray[np.float64]:
    """Evaluate the numerically stable equivalent expression."""
    return 1 / (np.sqrt(1 + x_values) + 1)


def display_error_results() -> None:
    """Display absolute and relative error measurements."""
    absolute_error, relative_error, percentage_error = calculate_errors()

    print("\nNUMERICAL ERROR ANALYSIS")
    print("-" * 40)

    print(f"Reference value: {np.sqrt(5):.8f}")
    print("Approximate value: 2.236")
    print(f"Absolute error: {absolute_error:.8f}")
    print(f"Relative error: {relative_error:.8f}")
    print(f"Percentage error: {percentage_error:.6f}%")


def display_stability_results() -> None:
    """Compare direct and numerically stable formulations."""
    x_values = np.array(
        [1e-4, 1e-8, 1e-12],
        dtype=np.float64,
    )

    direct_results = calculate_direct(x_values)
    stable_results = calculate_stable(x_values)

    differences = np.abs(direct_results - stable_results)

    print("\nNUMERICAL STABILITY COMPARISON")
    print("-" * 75)

    print(
        f"{'x':<12}"
        f"{'Direct expression':<25}"
        f"{'Stable expression':<25}"
        f"{'Difference':<15}"
    )

    for x, direct, stable, difference in zip(
        x_values,
        direct_results,
        stable_results,
        differences,
    ):
        print(
            f"{x:<12.0e}"
            f"{direct:<25.12f}"
            f"{stable:<25.12f}"
            f"{difference:<15.3e}"
        )


def main() -> None:
    """Execute the numerical error experiments."""
    demonstrate_float_comparison()
    display_error_results()
    display_stability_results()


if __name__ == "__main__":
    main()
