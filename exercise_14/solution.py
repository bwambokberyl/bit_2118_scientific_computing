
"""
File: exercise_14/solution.py
Purpose: Demonstrate numerical differentiation using finite differences.
Application: Estimating vehicle speed from GPS position measurements.
"""

import numpy as np
import matplotlib.pyplot as plt


def create_gps_measurements():
    """Create GPS time and position measurements."""
    time = np.array(
        [0, 1, 2, 3, 4, 5, 6],
        dtype=float
    )

    position = np.array(
        [0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0]
    )

    return time, position


def calculate_speed(time, position):
    """Estimate speed using forward, central, and backward differences."""
    speed = np.zeros_like(position)

    # Forward difference at the beginning.
    speed[0] = (
        position[1] - position[0]
    ) / (
        time[1] - time[0]
    )

    # Central differences for interior points.
    for i in range(1, len(time) - 1):
        speed[i] = (
            position[i + 1] - position[i - 1]
        ) / (
            time[i + 1] - time[i - 1]
        )

    # Backward difference at the end.
    speed[-1] = (
        position[-1] - position[-2]
    ) / (
        time[-1] - time[-2]
    )

    return speed


def display_results(time, position, speed):
    """Display position and estimated speed at each time."""
    print("NUMERICAL DIFFERENTIATION: GPS SPEED ESTIMATION")
    print("=" * 58)

    for t, x, v in zip(time, position, speed):
        print(
            f"t={t:.0f}s, "
            f"position={x:.1f}m, "
            f"estimated speed={v:.2f}m/s"
        )


def plot_speed(time, speed):
    """Plot estimated vehicle speed against time."""
    plt.figure(figsize=(9, 5))

    plt.plot(
        time,
        speed,
        marker="o",
        label="Estimated speed"
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Estimated speed (m/s)")
    plt.title("Speed Estimated from GPS Position Data")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    """Execute the numerical differentiation analysis."""
    time, position = create_gps_measurements()

    speed = calculate_speed(time, position)

    display_results(time, position, speed)

    plot_speed(time, speed)


if __name__ == "__main__":
    main()
