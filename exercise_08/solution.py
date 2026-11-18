
"""
File: exercise_08/solution.py
Purpose: Demonstrate eigenvalues and eigenvectors.
Application: Identifying influential nodes in a small
             undirected computer network.
"""

import numpy as np


def create_network():
    """Create the adjacency matrix of the computer network."""
    A = np.array([
        [0.0, 1.0, 1.0, 0.0],
        [1.0, 0.0, 1.0, 1.0],
        [1.0, 1.0, 0.0, 1.0],
        [0.0, 1.0, 1.0, 0.0]
    ])

    return A


def calculate_eigenvalues(A):
    """Calculate eigenvalues and eigenvectors of the matrix."""
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Identify the eigenvalue with the largest real part.
    index = np.argmax(np.real(eigenvalues))

    dominant_value = np.real(eigenvalues[index])
    dominant_vector = np.abs(
        np.real(eigenvectors[:, index])
    )

    return dominant_value, dominant_vector, eigenvectors, index


def calculate_centrality(dominant_vector):
    """Normalize the dominant eigenvector into importance scores."""
    centrality = dominant_vector / dominant_vector.sum()

    return centrality


def display_results(dominant_value, centrality, nodes):
    """Display the dominant eigenvalue and node importance scores."""
    print("EIGENVALUES AND EIGENVECTORS")
    print("=" * 42)

    print(f"\nDominant eigenvalue: {dominant_value:.6f}")

    print("\nEigenvector-based importance:")
    for node, score in zip(nodes, centrality):
        print(f"{node}: {score:.4f}")


def verify_eigenpair(A, dominant_value, eigenvectors, index):
    """Verify that Av is approximately equal to lambda times v."""
    v = np.real(eigenvectors[:, index])

    verification_error = np.linalg.norm(
        A @ v - dominant_value * v
    )

    print("\nVerification error:")
    print(f"{verification_error:.10e}")


def main():
    """Execute the network eigenvalue analysis."""
    nodes = ["A", "B", "C", "D"]

    A = create_network()

    dominant_value, dominant_vector, eigenvectors, index = (
        calculate_eigenvalues(A)
    )

    centrality = calculate_centrality(dominant_vector)

    display_results(dominant_value, centrality, nodes)

    verify_eigenpair(A, dominant_value, eigenvectors, index)


if __name__ == "__main__":
    main()
