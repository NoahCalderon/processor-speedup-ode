"""
CST-305 Project 1: Processor Speedup ODE 
Programmed and reviewed by Noah Calderon-Zuniga & Pisa Ripley
Packages: NumPy, SciPy, Matplotlib; Pythons built-in ast module   
second solve, and graph result. Model source: Project1_Notes, slide 7 
count is continous for calculus, with results shown as whole counts. 
"""


""" IMPORTS
    ast is used to safey parse user-entered expressions
    numpy  is used for arrays and numerical operations
    matplotlib.pyplot allows us to plot the speeduop curve
    solve_ivp from SciPy is a numerical ODE solver
    """
import ast
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#Check that equation entered contains only arithmetic and our variables. Reject unrecognized variable names, non-numeric constraints, and/or python constructs outside basic arithmetic.
def read_equation(text):
    tree = ast.parse(text, mode='eval')

    allowed = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
        ast.Name, ast.Load, ast.Add, ast.Sub, ast.Mult,
        ast.Div, ast.Pow, ast.UAdd, ast.USub
    )

    for part in ast.walk(tree):
        if not isinstance(part, allowed):
            raise ValueError(
                'Use only numbers, N, S, f, +, -, *, /, ** and parentheses.'
            )

        if isinstance(part, ast.Name) and part.id not in ('N', 'S', 'f'):
            raise ValueError('The only variables allowed are N, S and f.')

        if isinstance(part, ast.Constant):
            if type(part.value) not in (int, float):
                raise ValueError('Constants must be numbers.')

    return compile(tree, '<equation>', 'eval')

#Main Program
def main():
    print('Processor Speedup ODE')
    print('N = processors, S = speedup, f = parallel fraction')
    print('Press Enter at each prompt to use the example from notes.')

    default = 'f / ((1-f)*N + f)**2'
    equation = input(f'Enter dS/dN [{default}]: ').strip() or default
    formula = read_equation(equation)

    f = float(input('Parallel fraction, 0 to 1 [0.8]: ') or '0.8')
    maximum = int(input('Maximum processors, 2 to 1000 [16]: ') or '16')

    if not 0 <= f <= 1 or not 2 <= maximum <= 1000:
        raise ValueError('Use a fraction from 0 to 1 and 2 to 1000 processors.')

    # Calculate the slope for SciPy. ODE Definition.
    def ode(N, S):
        variables = {'N': N, 'S': S[0], 'f': f}
        return [eval(formula, {'__builtins__': {}}, variables)]

    counts = np.arange(1, maximum + 1)

    # Initial condition: one processor gives a speedup of 1.
    solution = solve_ivp(
        ode, (1, maximum), [1.0],
        t_eval=counts, rtol=1e-6, atol=1e-9
    )

    reference = solve_ivp(
        ode, (1, maximum), [1.0],
        t_eval=counts, rtol=1e-10, atol=1e-12
    )
    
    #The program raises ValueError and displays message to user if either solve reports failure
    if not solution.success or not reference.success:
        raise ValueError('Solver failed. Check the equation for undefined values.')
            
    speedup = solution.y[0]
    #Difference from a tighter solve estimates error; it is not a guaranteed bound.
    error = np.abs(speedup - reference.y[0])
    print(f'\ndS/dN = {equation}; S(1) = 1; f = {f}')
    print('Processors   Speedup(dimensionless)   Estimated absolute error')
    for i in range(len(counts)):
        print(f'{counts[i]:10d}   {speedup[i]:23.6f}   {error[i]:.2e}')
    print('Error estimate: differnece from a second solve with tighter tolerances.')
                
    # For the default model, also check the known solution from the notes.
    if equation.replace(' ', '') == default.replace(' ', ''):
        exact = 1/(1 - f + f / counts)
        print(f'Maximum error against Amdahl formula: {max(abs(speedup-exact)):.2e}')

    # Plot the computed speedup curve against processor count.
    plt.plot(counts, speedup, 'o-', label=f'Parallel fraction = {f:.0%}')
    plt.title('Processor Speedup: Numerical ODE Solution')
    plt.xlabel('Number of processors')
    plt.ylabel('Speedup relative to one processor (dimensionless)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


        
        
if __name__ == '__main__':
    try:
        main()
    except (ValueError, SyntaxError, ArithmeticError, TypeError) as error:
        print(f'Input or calculation error: {error}')
            



