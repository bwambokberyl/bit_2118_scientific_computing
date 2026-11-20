
import numpy as np
import matplotlib.pyplot as plt


# Simulation parameters
CAPACITY = 1000.0
MEAN_DEMAND = 850.0
STD_DEMAND = 120.0
N = 100_000

# Reproducible random number generator
rng = np.random.default_rng(42)


def simulate_demand():
    """
    Generate random demand scenarios using
    a normal probability distribution.
    """

    demand = rng.normal(
        MEAN_DEMAND,
        STD_DEMAND,
        N
    )

    return demand


def calculate_overload_probability(demand):
    """
    Identify overloaded scenarios and estimate
    the probability of server overload.
    """

    overloaded = demand > CAPACITY

    overload_probability = overloaded.mean()

    return overloaded, overload_probability


def calculate_running_probability(overloaded):
    """
    Calculate the running overload probability
    as the number of simulations increases.
    """

    running_probability = (
        np.cumsum(overloaded)
        / np.arange(1, N + 1)
    )

    return running_probability


def display_results(overloaded, overload_probability):
    """
    Display the simulation results.
    """

    print("MONTE CARLO SIMULATION RESULTS")
    print("--------------------------------")

    print(
        f"Estimated overload probability: "
        f"{overload_probability:.4%}"
    )

    print(
        f"Number of overload cases: "
        f"{overloaded.sum()} out of {N}"
    )


def plot_convergence(running_probability):
    """
    Plot how the estimated overload probability
    changes as more simulations are performed.
    """

    indices = np.unique(
        np.logspace(
            1,
            np.log10(N),
            200
        ).astype(int)
    ) - 1

    plt.figure(figsize=(10, 6))

    plt.semilogx(
        indices + 1,
        running_probability[indices]
    )

    plt.xlabel("Number of simulations")
    plt.ylabel("Estimated overload probability")

    plt.title(
        "Monte Carlo estimate of server-overload risk"
    )

    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    """
    Run the Monte Carlo server-overload simulation.
    """

    demand = simulate_demand()

    overloaded, overload_probability = (
        calculate_overload_probability(demand)
    )

    running_probability = (
        calculate_running_probability(overloaded)
    )

    display_results(
        overloaded,
        overload_probability
    )

    plot_convergence(running_probability)


if __name__ == "__main__":
    main()
