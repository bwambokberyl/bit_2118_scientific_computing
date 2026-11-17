"""
File: exercise_04/solution.py
Purpose: Demonstrate matrix algebra and 2-D geometric transformations.
Application: Scaling and rotating objects in computer graphics.
"""

import numpy as np
import numpy.typing as npt


def create_points() -> npt.NDArray[np.float64]:
    """Create the four coordinate points of a square."""
    return np.array(
        [
            [0.0, 0.0],
            [1.0, 0.0],
            [1.0, 1.0],
            [0.0, 1.0],
        ],
        dtype=np.float64,
    )


def create_transformation() -> npt.NDArray[np.float64]:
    """Create and combine rotation and scaling matrices."""
    angle = np.deg2rad(45)

    rotation = np.array(
        [
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)],
        ],
        dtype=np.float64,
    )

    scale = np.array(
        [
            [2.0, 0.0],
            [0.0, 1.5],
        ],
        dtype=np.float64,
    )

    # Apply scaling first, followed by rotation.
    transformation = rotation @ scale

    return transformation


def transform_points(
    points: npt.NDArray[np.float64],
    transformation: npt.NDArray[np.float64],
) -> npt.NDArray[np.float64]:
    """Apply the combined transformation to all coordinate points."""
    return points @ transformation.T


def display_results(
    points: npt.NDArray[np.float64],
    transformation: npt.NDArray[np.float64],
    transformed_points: npt.NDArray[np.float64],
) -> None:
    """Display the original and transformed coordinates."""
    determinant = np.linalg.det(transformation)

    print("MATRIX ALGEBRA AND 2-D OBJECT TRANSFORMATION")
    print("=" * 48)

    print("\nOriginal points:")
    print(points)

    print("\nCombined transformation matrix:")
    print(transformation)

    print("\nTransformed points:")
    print(transformed_points)

    print(f"\nDeterminant: {determinant:.6f}")

    if not np.isclose(determinant, 0.0):
        print("The transformation matrix is invertible.")
    else:
        print("The transformation matrix is singular.")


def main() -> None:
    """Execute the matrix transformation program."""
    points = create_points()
    transformation = create_transformation()

    transformed_points = transform_points(
        points,
        transformation,
    )

    display_results(
        points,
        transformation,
        transformed_points,
    )


if __name__ == "__main__":
    main()
