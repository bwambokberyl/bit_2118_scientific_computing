
"""
File: exercise_15/solution.py
Purpose: Demonstrate numerical integration using finite intervals.
Application: Estimating electrical energy from smart-meter readings.
"""

import numpy as np
from scipy.integrate import simpson


def create_measurements():
    """Create smart-meter time and power measurements."""
    time_hours = np.array(
        [0, 2, 4, 6, 8, 10, 12],
        dtype=float
    )

    power_kw = np.array(
        [0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9]
    )

    return time_hours, power_kw


def calculate_energy(time_hours, power_kw):
    """Calculate energy using trapezoidal and Simpson's rules."""
    energy_trapezoid = np.trapezoid(
        power_kw,
        time_hours
    )

    energy_simpson = simpson(
        power_kw,
        x=time_hours
    )

    return energy_trapezoid, energy_simpson


def display_results(energy_trapezoid, energy_simpson):
    """Display and compare the estimated energy consumption."""
    difference = abs(energy_simpson - energy_trapezoid)

    print("NUMERICAL INTEGRATION: ENERGY CONSUMPTION")
    print("=" * 52)

    print(
        f"\nEnergy using trapezoidal rule: "
        f"{energy_trapezoid:.3f} kWh"
    )

    print(
        f"Energy using Simpson's rule: "
        f"{energy_simpson:.3f} kWh"
    )

    print(
        f"Difference between estimates: "
        f"{difference:.3f} kWh"
    )


def main():
    """Execute the numerical integration analysis."""
    time_hours, power_kw = create_measurements()

    energy_trapezoid, energy_simpson = calculate_energy(
        time_hours,
        power_kw
    )

    display_results(
        energy_trapezoid,
        energy_simpson
    )


if __name__ == "__main__":
    main()
