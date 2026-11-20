
"""
File: exercise_17/solution.py
Purpose: Demonstrate numerical ODE solving using SciPy.
Application: Simulating the charging of an RC electrical circuit.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# RC circuit parameters
V_SUPPLY = 5.0
RESISTANCE = 1000.0
CAPACITANCE = 0.001
V_INITIAL = 0.0

START_TIME = 0.0
END_TIME = 5.0


def rc_circuit(t, voltage):
    """Define the differential equation for RC charging."""
    return [
        (V_SUPPLY - voltage[0])
        / (RESISTANCE * CAPACITANCE)
    ]


def solve_circuit():
    """Solve the RC charging differential equation using SciPy."""
    t_eval = np.linspace(START_TIME, END_TIME, 200)

    solution = solve_ivp(
        rc_circuit,
        (START_TIME, END_TIME),
        [V_INITIAL],
        t_eval=t_eval,
        rtol=1e-9,
        atol=1e-11
    )

    return solution


def calculate_exact_solution(time):
    """Calculate the analytical RC charging voltage."""
    exact = V_SUPPLY * (
        1 - np.exp(
            -time / (RESISTANCE * CAPACITANCE)
        )
    )

    return exact


def display_results(solution, exact):
    """Display solver status, final voltage, and maximum error."""
    maximum_error = np.max(
        np.abs(solution.y[0] - exact)
    )

    print("NUMERICAL ODE SOLUTION: RC CIRCUIT")
    print("=" * 48)

    print(f"\nSolver success: {solution.success}")

    print(
        f"Capacitor voltage at 5 s: "
        f"{solution.y[0, -1]:.4f} V"
    )

    print(
        f"Maximum error against exact solution: "
        f"{maximum_error:.3e} V"
    )


def plot_charging_curve(solution, exact):
    """Plot the numerical and exact charging curves."""
    plt.figure(figsize=(9, 5))

    plt.plot(
        solution.t,
        solution.y[0],
        label="solve_ivp"
    )

    plt.plot(
        solution.t,
        exact,
        linestyle="--",
        label="Exact solution"
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Capacitor voltage (V)")
    plt.title("RC Circuit Charging")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    """Execute the RC circuit simulation."""
    solution = solve_circuit()

    if not solution.success:
        print("Solver failed:", solution.message)
        return

    exact = calculate_exact_solution(solution.t)

    display_results(solution, exact)

    plot_charging_curve(solution, exact)


if __name__ == "__main__":
    main()
