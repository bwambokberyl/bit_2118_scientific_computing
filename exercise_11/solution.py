
"""
File: exercise_11/solution.py
Purpose: Demonstrate polynomial and nonlinear equation solving.
Application: Finding the intersection points of a circle
             and a parabola.
"""

import numpy as np
from scipy.optimize import root


def equations(z):
    """Define the nonlinear system using residual equations."""
    x, y = z

    return np.array([
        x**2 + y**2 - 4,
        y - (x**2 - 1)
    ])


def find_intersections(initial_guesses):
    """Find intersection points using different initial guesses."""
    solutions = []

    for guess in initial_guesses:
        solution = root(equations, guess)

        solutions.append((guess, solution))

    return solutions


def display_results(solutions):
    """Display intersection points and verify the residuals."""
    print("POLYNOMIAL AND NONLINEAR EQUATION SOLVING")
    print("=" * 55)

    for guess, solution in solutions:
        print(f"\nInitial guess: {guess}")
        print("Intersection:", solution.x)
        print("Residuals:", equations(solution.x))
        print("Converged:", solution.success)

        if not solution.success:
            print("Solver message:", solution.message)


def main():
    """Execute the nonlinear equation-solving analysis."""
    initial_guesses = [
        [1.0, 1.0],
        [-1.0, 1.0]
    ]

    solutions = find_intersections(initial_guesses)

    display_results(solutions)


if __name__ == "__main__":
    main()
