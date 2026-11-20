
import numpy as np
from scipy.optimize import minimize


# Server allocation parameters
COST_A = 12
COST_B = 18

CAPACITY_A = 100
CAPACITY_B = 170

REQUIRED_CAPACITY = 1000


def cost(z):
    """
    Calculate the total operating cost.

    z contains the allocation of Type A and Type B servers.
    """
    x, y = z
    return COST_A * x + COST_B * y


def capacity_constraint(z):
    """
    Ensure that the total processing capacity
    is at least the required capacity.
    """
    x, y = z

    return (
        CAPACITY_A * x
        + CAPACITY_B * y
        - REQUIRED_CAPACITY
    )


def optimize_allocation():
    """
    Find the continuous server allocation
    that minimizes operating cost.
    """

    constraints = {
        "type": "ineq",
        "fun": capacity_constraint
    }

    bounds = [(0, None), (0, None)]

    solution = minimize(
        cost,
        x0=[5, 3],
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    return solution


def find_best_integer_solution():
    """
    Search for the lowest-cost integer allocation
    that satisfies the capacity requirement.
    """

    best_integer = None

    for a in range(0, 20):
        for b in range(0, 20):

            capacity = (
                CAPACITY_A * a
                + CAPACITY_B * b
            )

            if capacity >= REQUIRED_CAPACITY:

                total_cost = COST_A * a + COST_B * b

                if (
                    best_integer is None
                    or total_cost < best_integer[0]
                ):
                    best_integer = (
                        total_cost,
                        a,
                        b,
                        capacity
                    )

    return best_integer


def display_results(solution, best_integer):
    """
    Display the continuous and integer optimization results.
    """

    print("CONTINUOUS OPTIMIZATION RESULTS")
    print("--------------------------------")

    print("Optimization success:", solution.success)

    if solution.success:
        x, y = solution.x

        capacity = (
            CAPACITY_A * x
            + CAPACITY_B * y
        )

        print(f"Type A allocation: {x:.3f}")
        print(f"Type B allocation: {y:.3f}")
        print(f"Total capacity: {capacity:.2f}")
        print(f"Minimum planning cost: {solution.fun:.2f}")

    else:
        print("Optimization failed:", solution.message)

    print("\nINTEGER OPTIMIZATION RESULTS")
    print("----------------------------")

    if best_integer is not None:
        total_cost, a, b, capacity = best_integer

        print(f"Type A servers: {a}")
        print(f"Type B servers: {b}")
        print(f"Total capacity: {capacity}")
        print(f"Minimum integer cost: {total_cost}")


def main():
    """
    Run the numerical optimization program.
    """

    solution = optimize_allocation()

    best_integer = find_best_integer_solution()

    display_results(solution, best_integer)


if __name__ == "__main__":
    main()
