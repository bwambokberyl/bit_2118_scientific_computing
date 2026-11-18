
"""
File: exercise_09/solution.py
Purpose: Demonstrate bisection and fixed-point methods.
Application: Determining the equilibrium temperature
             of a simplified thermal system.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar


def heat_balance(T):
    """Calculate the heat-balance function."""
    return T - 25 - 10 * np.exp(-T / 20)


def bisection_method():
    """Find the equilibrium temperature using bisection."""
    solution = root_scalar(
        heat_balance,
        bracket=[20, 40],
        method="bisect",
        xtol=1e-10
    )

    if not solution.converged:
        raise RuntimeError("Bisection method did not converge.")

    return solution


def fixed_point_method(initial_guess=30.0, tol=1e-10, max_iter=100):
    """Find the equilibrium temperature using fixed-point iteration."""

    def g(T):
        return 25 + 10 * np.exp(-T / 20)

    T = initial_guess
    history = [T]

    for _ in range(max_iter):
        T_new = g(T)
        history.append(T_new)

        if abs(T_new - T) < tol:
            return T_new, history

        T = T_new

    raise RuntimeError("Fixed-point method did not converge.")


def display_results(bisection_solution, fixed_point_solution, history):
    """Display the results obtained using both methods."""
    print("ROOT FINDING: BISECTION AND FIXED-POINT METHODS")
    print("=" * 55)

    print(
        f"\nBisection equilibrium temperature: "
        f"{bisection_solution.root:.6f} C"
    )

    print(
        f"Fixed-point equilibrium temperature: "
        f"{fixed_point_solution:.6f} C"
    )

    print(f"Fixed-point iterations: {len(history) - 1}")


def plot_equilibrium(solution):
    """Plot the heat-balance function and its equilibrium point."""
    temps = np.linspace(20, 40, 300)

    plt.figure(figsize=(9, 5))
    plt.plot(temps, heat_balance(temps), label="Heat-balance function")
    plt.axhline(0, linewidth=0.8)
    plt.axvline(
        solution.root,
        linestyle="--",
        label="Equilibrium temperature"
    )

    plt.xlabel("Temperature (C)")
    plt.ylabel("Heat-balance function")
    plt.title("Equilibrium Temperature")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    """Execute the root-finding analysis."""
    bisection_solution = bisection_method()

    fixed_point_solution, history = fixed_point_method()

    display_results(
        bisection_solution,
        fixed_point_solution,
        history
    )

    plot_equilibrium(bisection_solution)


if __name__ == "__main__":
    main()
