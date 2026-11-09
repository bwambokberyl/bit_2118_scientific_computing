"""
File: exercise_02_numpy_arrays/solution.py

Purpose:
Demonstrate NumPy arrays, statistical calculations,
and vectorized unit conversion using air-quality data.
"""

import numpy as np
import numpy.typing as npt


def load_data() -> npt.NDArray[np.float64]:
    """Create an array containing 24 hourly PM2.5 measurements."""
    readings = np.array(
        [
            12.4, 11.8, 10.9, 10.2, 11.1, 13.6,
            18.2, 22.5, 26.1, 29.4, 31.0, 28.7,
            27.3, 25.8, 24.6, 23.1, 21.7, 20.4,
            19.2, 18.0, 16.8, 15.5, 14.3, 13.1,
        ],
        dtype=np.float64,
    )

    return readings


def calculate_statistics(
    readings: npt.NDArray[np.float64],
) -> tuple[float, float, float]:
    """Calculate mean, minimum, and maximum measurements."""
    mean_value = float(np.mean(readings))
    min_value = float(np.min(readings))
    max_value = float(np.max(readings))

    return mean_value, min_value, max_value


def convert_units(
    readings: npt.NDArray[np.float64],
) -> npt.NDArray[np.float64]:
    """Convert PM2.5 measurements from µg/m³ to mg/m³."""
    return readings / 1000


def display_results(
    readings: npt.NDArray[np.float64],
    converted: npt.NDArray[np.float64],
) -> None:
    """Display the calculated statistical results."""
    mean_value, min_value, max_value = calculate_statistics(readings)

    print("AIR QUALITY MONITORING REPORT")
    print("-" * 35)

    print(f"Number of readings: {len(readings)}")
    print(f"Daily mean: {mean_value:.2f} µg/m³")
    print(f"Minimum: {min_value:.2f} µg/m³")
    print(f"Maximum: {max_value:.2f} µg/m³")

    print("\nFirst six converted readings (mg/m³):")
    print(np.round(converted[:6], 4))

    print("\nVerification:")
    print(f"Array dimensions: {readings.ndim}")
    print(f"Array shape: {readings.shape}")
    print(f"Conversion successful: {len(converted) == len(readings)}")


def main() -> None:
    """Execute the air-quality numerical computation."""
    readings = load_data()

    converted = convert_units(readings)

    display_results(readings, converted)


if __name__ == "__main__":
    main()