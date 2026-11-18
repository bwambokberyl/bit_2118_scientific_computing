
"""
File: exercise_06/solution.py
Purpose: Demonstrate Gaussian Elimination and LU Decomposition.
Application: Repeatedly solving linear systems using the same
             coefficient matrix and different measurement vectors.
"""

import numpy as np
from scipy.linalg import lu_factor, lu_solve


def create_system():
    """Create the coefficient matrix and measurement vectors."""

    A = np.array([
        [4.0, -1.0, 0.0],
        [-1.0, 4.0, -1.0],
        [0.0, -1.0, 3.0]
    ])

    measurement_sets = [
        np.array([15.0, 10.0, 10.0]),
        np.array([16.0, 11.0, 9.0]),
        np.array([14.0, 12.0, 11.0])
    ]

    return A, measurement_sets


def factorize_matrix(A):
    """Factorize the coefficient matrix once using LU decomposition."""

    lu, piv = lu_factor(A)

    return lu, piv


def solve_measurements(A, measurement_sets, lu, piv):
    """Solve each measurement system using the stored LU factors."""

    results = []

    for i, b in enumerate(measurement_sets, start=1):

        solution = lu_solve((lu, piv), b)

        residual = b - A @ solution

        residual_norm = np.linalg.norm(residual)

        results.append(
            (i, solution, residual, residual_norm)
        )

    return results


def display_results(results):
    """Display the solutions and verification results."""

    print("GAUSSIAN ELIMINATION AND LU DECOMPOSITION")
    print("=" * 52)

    for i, solution, residual, residual_norm in results:

        print(f"\nMeasurement Set {i}")
        print("-" * 25)

        print("Solution:", solution)

        print("Residual:", residual)

        print(f"Residual norm: {residual_norm:.8f}")


def compare_direct_solution(A, measurement_sets):
    """Compare the first LU solution with a direct NumPy solution."""

    direct_solution = np.linalg.solve(A, measurement_sets[0])

    print("\nDirect solution for first measurement set:")
    print(direct_solution)


def main():
    """Execute the LU decomposition demonstration."""

    A, measurement_sets = create_system()

    # Factorize the coefficient matrix only once.
    lu, piv = factorize_matrix(A)

    # Reuse the LU factors for all measurement vectors.
    results = solve_measurements(
        A, measurement_sets, lu, piv
    )

    display_results(results)

    # Compare with a direct solution.
    compare_direct_solution(A, measurement_sets)


if __name__ == "__main__":
    main()
