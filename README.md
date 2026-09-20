# Processor Speedup ODE  
CST‑305 Project 1 — Visualizing a Differential Equation with SciPy  
Programmed and reviewed by Noah Calderon‑Zuniga & Pisa Ripley

---

## Overview

This project numerically solves and visualizes a differential equation that models processor speedup in parallel computing. The mathematical model is based on the differential form of Amdahl’s Law, which describes how performance improves when a portion of a program can run in parallel across multiple processors.

Instead of using the closed‑form Amdahl expression, the program solves the initial value problem



$$
\frac{dS}{dN} = \frac{f}{((1-f)N + f)^2}, \quad S(1) = 1
$$




where  
- \( N \) is the number of processors,  
- \( S(N) \) is the speedup,  
- \( f \) is the parallel fraction of the workload.

The program allows users to enter their own differential equation, choose a parallel fraction, and select a maximum processor count. It then computes the numerical solution, estimates numerical error, and plots the resulting speedup curve.

---

## Features

- Safe parsing of user‑entered ODE expressions using Python’s `ast` module  
- Numerical ODE solving using SciPy’s `solve_ivp`  
- Dual‑tolerance solving for numerical error estimation  
- Optional comparison to the exact Amdahl formula  
- Clean terminal output of processor counts, speedup values, and error estimates  
- Matplotlib visualization of the speedup curve  

---

## Requirements

This project requires the following Python packages:

- NumPy  
- SciPy  
- Matplotlib  

Python’s built‑in `ast` module is used for safe expression parsing.

---

## Installation

### Installing in PyCharm (recommended)

1. Clone or download the repository from GitHub.  
2. Open the project folder in PyCharm.  
3. When prompted, allow PyCharm to create a virtual environment.  
4. Open the terminal inside PyCharm and install dependencies: pip install numpy scipy matplotlib


## Running the Program

### In PyCharm

1. Open the main Python file (for example, `processor_speedup_ode.py`).  
2. Click the green Run button in the top‑right corner.  
3. Follow the prompts in the terminal window.


---

## User Input

When the program starts, it will prompt for three inputs:

### 1. Differential equation for dS/dN  
You may enter any valid expression using only  
`N`, `S`, `f`, numbers, and arithmetic operators.  
Press Enter to use the default equation from the CST‑305 notes.

### 2. Parallel fraction f  
Must be between 0 and 1.  
Press Enter to use the default value of 0.8.

### 3. Maximum number of processors  
Must be between 2 and 1000.  
Press Enter to use the default value of 16.

Invalid input will produce a clear error message.

---

## Output

The program prints:

- A table of processor counts  
- The numerical speedup at each count  
- An estimated numerical error based on a tighter reference solve  

If the default ODE is used, the program also computes the exact Amdahl speedup and prints the maximum difference between the numerical and analytical results.

Finally, the program displays a Matplotlib graph showing:

- Processor count on the horizontal axis  
- Speedup on the vertical axis  
- A curve representing the numerical ODE solution  

---

## Troubleshooting

### Windows Smart App Control

Some Windows systems may block SciPy’s numerical libraries, causing errors such as:


To fix this:

1. Open **Windows Security**  
2. Select **App & Browser Control**  
3. Open **Smart App Control settings**  
4. Turn Smart App Control **Off**  
5. Restart your computer  
6. Recreate your virtual environment and reinstall SciPy

### Plot Window Not Appearing in PyCharm

If the graph does not appear:

- Enable “Show plots in tool window” in  
  **File → Settings → Tools → Python Scientific**  
- Or disable it to force a separate pop‑up window  
- Add `matplotlib.use('TkAgg')` if needed  
- Run the script outside PyCharm to confirm the environment is working

---

## License

This project is for academic use in CST‑305 at Grand Canyon University.




