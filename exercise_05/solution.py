"""
File: exercise_05/solution.py
Purpose: Solve a system of linear equations using NumPy.
Application: Determining the number of active servers
             from their total CPU and memory consumption.
"""

import numpy as np


def create_system():
    """Create the coefficient matrix and constant vector."""

    # x = number of Type A servers
    # y = number of Type B servers

    # Type A uses 4 CPU units and 8 GB memory.
    # Type B uses 2 CPU units and 12 GB memory.
    #
    # Total CPU usage = 20 units
    # Total memory usage = 72 GB

    A = np.array([
        [4.0, 2.0],
        [8.0, 12.0]
    ])

    b = np.array([20.0, 72.0])

    return A, b


def solve_system(A, b):
    """Solve the system Ax = b."""

    solution = np.linalg.solve(A, b)

    return solution


def verify_solution(A, b, solution):
    """Verify the solution using matrix multiplication."""

    calculated_values = A @ solution

    residual = b - calculated_values

    residual_norm = np.linalg.norm(residual)

    return calculated_values, residual, residual_norm


def display_results(solution, calculated_values, residual, residual_norm):
    """Display the calculated solution and verification results."""

    print("SOLUTION OF SYSTEMS OF LINEAR EQUATIONS")
    print("=" * 48)

    print("\nCalculated number of servers:")
    print(f"Type A servers: {solution[0]:.0f}")
    print(f"Type B servers: {solution[1]:.0f}")

    print("\nVerification using A @ solution:")
    print(calculated_values)

    print("\nResidual:")
    print(residual)

    print(f"\nResidual norm: {residual_norm:.6f}")

    if np.allclose(residual, 0):
        print("\nVerification successful: The solution is correct.")
    else:
        print("\nVerification failed: Check the calculated solution.")


def main():
    """Execute the linear system solution."""

    A, b = create_system()

    solution = solve_system(A, b)

    calculated_values, residual, residual_norm = verify_solution(
        A, b, solution
    )

    display_results(
        solution,
        calculated_values,
        residual,
        residual_norm
    )


if __name__ == "__main__":
    main()
