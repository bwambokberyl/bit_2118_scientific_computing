
"""
File: exercise_13/solution.py
Purpose: Demonstrate curve fitting using the least-squares method.
Application: Modelling server response time against concurrent users.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def create_measurements():
    """Create the server load and response-time measurements."""
    users = np.array(
        [50, 100, 150, 200, 250, 300, 350],
        dtype=float
    )

    response_ms = np.array(
        [82, 95, 115, 145, 185, 238, 305],
        dtype=float
    )

    return users, response_ms


def quadratic_model(x, a, b, c):
    """Define the quadratic model used for curve fitting."""
    return a * x**2 + b * x + c


def fit_curve(users, response_ms):
    """Estimate the parameters of the quadratic model."""
    parameters, covariance = curve_fit(
        quadratic_model,
        users,
        response_ms
    )

    return parameters, covariance


def calculate_errors(response_ms, predicted):
    """Calculate the residuals and root mean square error."""
    residuals = response_ms - predicted
    rmse = np.sqrt(np.mean(residuals**2))

    return residuals, rmse


def display_results(parameters, rmse):
    """Display the fitted model and prediction at 400 users."""
    a, b, c = parameters

    prediction = quadratic_model(400, a, b, c)

    print("CURVE FITTING: SERVER RESPONSE TIME")
    print("=" * 48)

    print(
        f"\nFitted model: y = {a:.6f}x^2 "
        f"+ {b:.4f}x + {c:.2f}"
    )

    print(f"RMSE: {rmse:.2f} ms")

    print(
        f"Predicted response at 400 users: "
        f"{prediction:.2f} ms"
    )


def plot_curve(users, response_ms, parameters):
    """Plot the measured data and fitted quadratic curve."""
    x_plot = np.linspace(users.min(), 400, 300)

    y_plot = quadratic_model(x_plot, *parameters)

    plt.figure(figsize=(9, 5))

    plt.scatter(
        users,
        response_ms,
        label="Measurements"
    )

    plt.plot(
        x_plot,
        y_plot,
        label="Fitted curve"
    )

    plt.xlabel("Concurrent users")
    plt.ylabel("Response time (ms)")
    plt.title("Server Response-Time Curve Fitting")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    """Execute the curve-fitting analysis."""
    users, response_ms = create_measurements()

    parameters, covariance = fit_curve(
        users,
        response_ms
    )

    predicted = quadratic_model(users, *parameters)

    residuals, rmse = calculate_errors(
        response_ms,
        predicted
    )

    display_results(parameters, rmse)

    plot_curve(users, response_ms, parameters)


if __name__ == "__main__":
    main()
