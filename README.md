
# Scientific Computing — BIT 2118

A collection of 19 practical scientific computing exercises implemented in Python as part of the **BIT 2118 Scientific Computing** unit.

This repository explores numerical methods and computational techniques used to solve mathematical and real-world problems. Each exercise focuses on a specific scientific computing concept and demonstrates its application through a practical problem.

The implementations use Python libraries such as **NumPy**, **SciPy**, and **Matplotlib** for numerical computation, scientific analysis, optimization, and visualization.

The goal of this repository is to develop a practical understanding of numerical methods by connecting mathematical concepts to problems involving technology, engineering, data analysis, computing systems, and everyday applications.

## Repository Structure

The repository is organized into individual exercise directories. Each exercise contains its own documentation and Python implementation, while execution screenshots are stored in a shared `output_images/` directory.

```text
scientific-computing/
│
├── README.md
│
├── exercise_01/
│   ├── README.md
│   └── solution.py
│
├── exercise_02/
│   ├── README.md
│   └── solution.py
│
├── exercise_03/
│   ├── README.md
│   └── solution.py
│
├── ...
│
├── exercise_19/
│   ├── README.md
│   └── solution.py
│
└── output_images/
    ├── exercise_01.png
    ├── exercise_02.png
    ├── exercise_03.png
    ├── ...
    └── exercise_19.png
```

### Exercise Organization

Each exercise directory contains two main files:

- **README.md:** Explains the mathematical concept, worked example, real-world applications, problem being addressed, solution approach, and implementation.
- **solution.py:** Contains the Python implementation of the numerical method.

The `output_images/` directory contains screenshots of actual program execution. These screenshots provide evidence of the program output and visualizations where applicable.

Each exercise's README includes its corresponding screenshot for easy reference.

## Exercise Index

The following table provides an overview of the numerical methods explored in the repository and the practical problems addressed in each exercise.

| # | Directory | Numerical Topic | Real-World Application |
|---|---|---|---|
| 01 | [exercise_01](exercise_01/) | NumPy Arrays and Numerical Computation | Processing weather-station temperature readings and performing statistical calculations |
| 02 | [exercise_02](exercise_02/) | Mathematical Functions and Vectorization | Processing large network-latency datasets efficiently using vectorized operations |
| 03 | [exercise_03](exercise_03/) | Floating-Point Arithmetic and Numerical Errors | Monitoring small structural deformations while understanding numerical precision and error |
| 04 | [exercise_04](exercise_04/) | Matrix Algebra and Matrix Operations | Performing mathematical transformations and manipulating coordinate data |
| 05 | [exercise_05](exercise_05/) | Solution of Systems of Linear Equations | Determining the number of server types from their combined CPU and memory usage |
| 06 | [exercise_06](exercise_06/) | Gaussian Elimination and LU Decomposition | Reusing matrix factorization to solve repeated engineering and measurement systems |
| 07 | [exercise_07](exercise_07/) | Iterative Methods for Linear Systems | Solving large systems of grid-based temperature equations using Jacobi and Gauss-Seidel methods |
| 08 | [exercise_08](exercise_08/) | Eigenvalues and Eigenvectors | Analyzing network relationships and identifying influential nodes using eigenvector centrality |
| 09 | [exercise_09](exercise_09/) | Root Finding: Bisection and Fixed-Point Methods | Finding the equilibrium temperature in a heat-balance problem |
| 10 | [exercise_10](exercise_10/) | Root Finding: Newton-Raphson and Secant Methods | Calculating the internal rate of return of a financial investment |
| 11 | [exercise_11](exercise_11/) | Polynomial and Nonlinear Equation Solving | Finding the intersection points of a circle and a parabola |
| 12 | [exercise_12](exercise_12/) | Interpolation | Estimating missing temperature measurements from sensor data |
| 13 | [exercise_13](exercise_13/) | Curve Fitting and Approximation | Modelling server response time as the number of concurrent users increases |
| 14 | [exercise_14](exercise_14/) | Numerical Differentiation | Estimating vehicle speed from GPS position measurements |
| 15 | [exercise_15](exercise_15/) | Numerical Integration | Estimating energy consumption from smart-meter power measurements |
| 16 | [exercise_16](exercise_16/) | Ordinary Differential Equations: Euler Method | Modelling temperature changes using Newton's law of cooling |
| 17 | [exercise_17](exercise_17/) | Numerical Solution of ODEs Using SciPy | Simulating the charging behaviour of a capacitor in an RC circuit |
| 18 | [exercise_18](exercise_18/) | Numerical Optimization | Minimizing cloud server operating costs while satisfying processing-capacity requirements |
| 19 | [exercise_19](exercise_19/) | Random Numbers and Monte Carlo Methods | Estimating the probability of server overload under uncertain network demand |

## Technologies and Libraries

The exercises are implemented using Python and the following scientific computing libraries:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| NumPy | Numerical operations, arrays, matrices, and random number generation |
| SciPy | Scientific algorithms, equation solving, optimization, interpolation, and integration |
| Matplotlib | Data visualization and plotting |
| Git and GitHub | Version control and project documentation |

## Setup and Usage

### 1. Clone the repository

```bash
git clone git@github.com:bwambokberyl/bit_2118_scientific_computing.git
cd scientific-computing
```

### 2. Create a virtual environment

```bash
python3 -m venv ~/.venvs/scientific-computing
```

### 3. Activate the virtual environment

On Linux:

```bash
source ~/.venvs/scientific-computing/bin/activate
```

### 4. Install the required libraries

```bash
pip install numpy scipy matplotlib
```

### 5. Run an exercise

Navigate to the repository root and execute the Python file for the exercise you want to run.

For example, to run Exercise 19:

```bash
python exercise_19/solution.py
```

You can replace `exercise_19` with any other exercise directory.

## Learning Approach

The exercises follow a practical, problem-oriented approach to scientific computing.

Each exercise generally follows this sequence:

1. **Mathematical Concept:** Introduces the numerical method and the mathematical principles behind it.
2. **Worked Example:** Demonstrates the concept using a simple mathematical example.
3. **Real-World Applications:** Explores where the method is used in practical situations.
4. **Problem and Solution Approach:** Identifies a real-world problem and explains how the numerical method can be applied.
5. **Implementation:** Translates the mathematical approach into executable Python code.
6. **Execution and Visualization:** Runs the implementation and documents the actual results.

This structure makes it possible to understand not only how a numerical method works, but also why it is useful and where it can be applied.

