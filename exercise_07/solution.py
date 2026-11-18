
"""
File: exercise_07/solution.py
Purpose: Demonstrate Jacobi and Gauss-Seidel iterative methods.
Application: Estimating steady-state temperatures at five
             interior points in a simplified temperature model.
"""

import numpy as np
import matplotlib.pyplot as plt


# Simplified steady-state temperature model.
# Left boundary = 100 degrees Celsius.
# Right boundary = 20 degrees Celsius.

A = np.array([
    [2.0, -1.0, 0.0, 0.0, 0.0],
    [-1.0, 2.0, -1.0, 0.0, 0.0],
    [0.0, -1.0, 2.0, -1.0, 0.0],
    [0.0, 0.0, -1.0, 2.0, -1.0],
    [0.0, 0.0, 0.0, -1.0, 2.0]
])

b = np.array([100.0, 0.0, 0.0, 0.0, 20.0])


def jacobi(A, b, tol=1e-8, max_iter=500):
    """Solve a linear system using the Jacobi method."""

    D = np.diag(A)
    R = A - np.diagflat(D)

    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):

        x_new = (b - R @ x) / D

        error = np.linalg.norm(x_new - x, ord=np.inf)

        errors.append(error)

        if error < tol:
            return x_new, errors

        x = x_new

    return x, errors


def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    """Solve a linear system using the Gauss-Seidel method."""

    x = np.zeros_like(b)
    errors = []

    for _ in range(max_iter):

        old = x.copy()

        for i in range(len(b)):

            x[i] = (
                b[i]
                - A[i, :i] @ x[:i]
                - A[i, i + 1:] @ old[i + 1:]
            ) / A[i, i]

        error = np.linalg.norm(x - old, ord=np.inf)

        errors.append(error)

        if error < tol:
            return x, errors

    return x, errors


def display_results(x_j, err_j, x_gs, err_gs, x_exact):
    """Display the temperature estimates and convergence results."""

    print("ITERATIVE METHODS FOR LINEAR SYSTEMS")
    print("=" * 48)

    print("\nJacobi temperatures:")
    print(x_j)

    print("\nGauss-Seidel temperatures:")
    print(x_gs)

    print("\nDirect solution:")
    print(x_exact)

    print("\nConvergence information:")
    print(f"Jacobi iterations: {len(err_j)}")
    print(f"Gauss-Seidel iterations: {len(err_gs)}")

    print(f"\nJacobi final change: {err_j[-1]:.10e}")
    print(f"Gauss-Seidel final change: {err_gs[-1]:.10e}")

    print("\nResidual norms:")

    print(
        "Jacobi:",
        f"{np.linalg.norm(b - A @ x_j):.10e}"
    )

    print(
        "Gauss-Seidel:",
        f"{np.linalg.norm(b - A @ x_gs):.10e}"
    )


def plot_convergence(err_j, err_gs):
    """Plot the convergence of both iterative methods."""

    plt.figure(figsize=(9, 5))

    plt.semilogy(err_j, label="Jacobi")
    plt.semilogy(err_gs, label="Gauss-Seidel")

    plt.xlabel("Iteration")
    plt.ylabel("Maximum change")
    plt.title("Convergence of Iterative Temperature Solution")

    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def main():
    """Execute the iterative temperature model."""

    x_j, err_j = jacobi(A, b)

    x_gs, err_gs = gauss_seidel(A, b)

    x_exact = np.linalg.solve(A, b)

    display_results(
        x_j, err_j,
        x_gs, err_gs,
        x_exact
    )

    plot_convergence(err_j, err_gs)


if __name__ == "__main__":
    main()

