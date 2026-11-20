# Scientific Computing — BIT 2118

A collection of 19 scientific computing exercises implemented in Python using **NumPy**, **SciPy**, and **Matplotlib**. Each exercise explores a numerical method and demonstrates its application to a practical real-world problem.

## Repository Structure

```text
scientific-computing/
├── README.md
├── exercise_01/
│   ├── README.md
│   └── solution.py
├── exercise_02/
│   ├── README.md
│   └── solution.py
├── ...
├── exercise_19/
│   ├── README.md
│   └── solution.py
└── output_images/
    ├── exercise_01.png
    ├── exercise_02.png
    └── ...
```

Each exercise contains:
- `README.md` — Mathematical concepts, examples, applications, and solution approach.
- `solution.py` — Python implementation.
- `output_images/` — Screenshots of actual program execution, stored centrally.

## Exercise Index

| # | Numerical Topic | Real-World Application |
|---|---|---|
| 01 | NumPy Arrays | Weather data analysis |
| 02 | Vectorization and Dot Products | Network latency calculations |
| 03 | Floating-Point Errors | Numerical precision in measurements |
| 04 | Matrix Algebra | Coordinate transformations |
| 05 | Linear Systems | Server resource calculations |
| 06 | LU Decomposition | Solving engineering systems |
| 07 | Iterative Solvers | Grid-based temperature calculations |
| 08 | Eigenvalues and Eigenvectors | Network centrality analysis |
| 09 | Bisection and Fixed-Point Methods | Heat balance calculations |
| 10 | Newton-Raphson and Secant Methods | Investment return calculations |
| 11 | Nonlinear Equations | Geometric intersection problems |
| 12 | Interpolation | Temperature sensor estimation |
| 13 | Curve Fitting | Server performance modelling |
| 14 | Numerical Differentiation | Vehicle speed estimation |
| 15 | Numerical Integration | Energy consumption estimation |
| 16 | ODEs: Euler Method | Newton's law of cooling |
| 17 | ODEs Using SciPy | RC circuit simulation |
| 18 | Numerical Optimization | Cloud server cost optimization |
| 19 | Monte Carlo Methods | Server overload risk estimation |

## Setup and Usage

**1. Clone the repository**

```bash
git clone https://github.com/bwambokberyl/bit_2118_scientific_computing.git
cd scientific-computing
```

**2. Create and activate a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install numpy scipy matplotlib
```

**4. Run an exercise**

```bash
python exercise_19/solution.py
```

Replace `exercise_19` with the exercise you want to run.

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib
- Git and GitHub