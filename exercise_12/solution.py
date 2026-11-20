
"""
File: exercise_12/solution.py
Purpose: Demonstrate linear and cubic spline interpolation.
Application: Estimating temperature measurements between
             hourly sensor readings.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline


def create_measurements():
    """Create the hourly temperature measurements."""
    hours = np.array(
        [8, 9, 10, 11, 12, 13, 14],
        dtype=float
    )

    temperature = np.array(
        [18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0]
    )

    return hours, temperature


def create_interpolation_functions(hours, temperature):
    """Create linear and cubic spline interpolation functions."""
    linear = interp1d(hours, temperature, kind="linear")

    cubic = CubicSpline(hours, temperature)

    return linear, cubic


def estimate_temperatures(linear, cubic):
    """Estimate temperatures at 10-minute intervals."""
    # 37 points create 36 equal intervals across six hours.
    ten_minute_times = np.linspace(8, 14, 37)

    linear_estimates = linear(ten_minute_times)
    cubic_estimates = cubic(ten_minute_times)

    return ten_minute_times, linear_estimates, cubic_estimates


def display_results(linear, cubic):
    """Display temperature estimates at 10:30."""
    target_time = 10.5

    linear_estimate = float(linear(target_time))
    cubic_estimate = float(cubic(target_time))

    print("INTERPOLATION: LINEAR AND CUBIC SPLINE")
    print("=" * 48)

    print(
        f"\nLinear estimate at 10:30: "
        f"{linear_estimate:.2f} C"
    )

    print(
        f"Cubic estimate at 10:30: "
        f"{cubic_estimate:.2f} C"
    )


def plot_interpolation(
    hours,
    temperature,
    ten_minute_times,
    linear_estimates,
    cubic_estimates
):
    """Plot original measurements and interpolation curves."""
    plt.figure(figsize=(9, 5))

    plt.scatter(
        hours,
        temperature,
        label="Hourly measurements"
    )

    plt.plot(
        ten_minute_times,
        linear_estimates,
        label="Linear"
    )

    plt.plot(
        ten_minute_times,
        cubic_estimates,
        label="Cubic spline"
    )

    plt.xlabel("Hour of day")
    plt.ylabel("Temperature (C)")
    plt.title("Temperature Interpolation")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    """Execute the temperature interpolation analysis."""
    hours, temperature = create_measurements()

    linear, cubic = create_interpolation_functions(
        hours,
        temperature
    )

    ten_minute_times, linear_estimates, cubic_estimates = (
        estimate_temperatures(linear, cubic)
    )

    display_results(linear, cubic)

    plot_interpolation(
        hours,
        temperature,
        ten_minute_times,
        linear_estimates,
        cubic_estimates
    )


if __name__ == "__main__":
    main()
