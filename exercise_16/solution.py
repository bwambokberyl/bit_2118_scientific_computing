
"""
File: exercise_16/solution.py
Purpose: Demonstrate solving an ordinary differential equation
         using Euler's numerical method.
Application: Predicting the cooling of a hot object.
"""

import numpy as np
import matplotlib.pyplot as plt


# Cooling model parameters
T_AMBIENT = 25.0
T_INITIAL = 90.0
K = 0.12

STEP_SIZE = 1.0
END_TIME = 30.0


def cooling_rate(temperature):
    """Calculate the cooling rate using Newton's law of cooling."""
    return -K * (temperature - T_AMBIENT)


def calculate_euler_solution(time):
    """Estimate temperature values using Euler's method."""
    temperature = np.zeros_like(time)

    temperature[0] = T_INITIAL

    for i in range(len(time) - 1):
        temperature[i + 1] = (
            temperature[i]
            + STEP_SIZE * cooling_rate(temperature[i])
        )

    return temperature


def calculate_exact_solution(time):
    """Calculate the analytical solution for Newton's law of cooling."""
    exact = (
        T_AMBIENT
        + (T_INITIAL - T_AMBIENT) * np.exp(-K * time)
    )

    return exact


def display_results(temperature, exact):
    """Display final temperatures and the numerical error."""
    error = abs(temperature[-1] - exact[-1])

    print("ORDINARY DIFFERENTIAL EQUATIONS: EULER METHOD")
    print("=" * 55)

    print(
        f"\nEuler temperature after 30 min: "
        f"{temperature[-1]:.2f} C"
    )

    print(
        f"Exact temperature after 30 min: "
        f"{exact[-1]:.2f} C"
    )

    print(
        f"Final absolute error: {error:.4f} C"
    )


def plot_cooling(time, temperature, exact):
    """Plot Euler's approximation against the exact solution."""
    plt.figure(figsize=(9, 5))

    plt.plot(
        time,
        temperature,
        marker="o",
        label="Euler"
    )

    plt.plot(
        time,
        exact,
        label="Exact solution"
    )

    plt.xlabel("Time (minutes)")
    plt.ylabel("Temperature (C)")
    plt.title("Cooling of a Hot Object")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    """Execute the Euler method cooling simulation."""
    time = np.arange(
        0,
        END_TIME + STEP_SIZE,
        STEP_SIZE
    )

    temperature = calculate_euler_solution(time)

    exact = calculate_exact_solution(time)

    display_results(temperature, exact)

    plot_cooling(time, temperature, exact)


if __name__ == "__main__":
    main()
