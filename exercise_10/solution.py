
"""
File: exercise_10/solution.py
Purpose: Demonstrate Newton-Raphson and Secant methods.
Application: Calculating the internal rate of return (IRR)
             of an investment using its cash flows.
"""

from scipy.optimize import root_scalar


# Initial investment followed by annual cash inflows.
cash_flows = [-10000, 3000, 3500, 4000, 2500]


def npv(rate):
    """Calculate the net present value at a given rate."""
    return sum(
        cf / (1 + rate) ** t
        for t, cf in enumerate(cash_flows)
    )


def d_npv(rate):
    """Calculate the derivative of the NPV function."""
    return sum(
        -t * cf / (1 + rate) ** (t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )


def newton_raphson_method():
    """Calculate the IRR using the Newton-Raphson method."""
    solution = root_scalar(
        npv,
        fprime=d_npv,
        x0=0.10,
        method="newton",
        xtol=1e-12
    )

    if not solution.converged:
        raise RuntimeError("Newton-Raphson method did not converge.")

    return solution


def secant_method():
    """Calculate the IRR using the Secant method."""
    solution = root_scalar(
        npv,
        x0=0.05,
        x1=0.20,
        method="secant",
        xtol=1e-12
    )

    if not solution.converged:
        raise RuntimeError("Secant method did not converge.")

    return solution


def display_results(newton_solution, secant_solution):
    """Display the calculated IRR values and verification."""
    print("ROOT FINDING: NEWTON-RAPHSON AND SECANT METHODS")
    print("=" * 55)

    print(
        f"\nIRR using Newton-Raphson: "
        f"{newton_solution.root:.6%}"
    )

    print(
        f"IRR using Secant method: "
        f"{secant_solution.root:.6%}"
    )

    print(
        f"NPV at Newton solution: "
        f"{npv(newton_solution.root):.6f}"
    )


def main():
    """Execute the financial root-finding analysis."""
    newton_solution = newton_raphson_method()
    secant_solution = secant_method()

    display_results(newton_solution, secant_solution)


if __name__ == "__main__":
    main()
