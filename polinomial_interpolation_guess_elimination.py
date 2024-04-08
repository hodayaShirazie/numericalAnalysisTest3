from colors import bcolors
from matrix_utility import *
from gaussian_elimination import gaussianElimination
import numpy as np


def create_matrix_with_b_col(matrix, b):
    if len(matrix) != len(b):
        raise ValueError("Number of rows in matrix and b must be the same")

    new_matrix = []
    for i in range(len(matrix)):
        new_row = matrix[i] + [b[i][0]]
        new_matrix.append(new_row)

    return new_matrix





def solve_mat_my_method(augmented_matrix):
    # Directly use augmented_matrix for gaussianElimination
    solution = gaussianElimination(augmented_matrix)
    return np.array(solution)

def polynomialInterpolation(table_points, x):
    n = len(table_points)
    matrix = [[point[0] ** i for i in range(n)] for point in table_points]
    b = [[point[1]] for point in table_points]


    matrix_np = np.array(matrix)
    b_np = np.array(b)
    augmented_matrix = np.hstack((matrix_np, b_np))


    sol = solve_mat_my_method(augmented_matrix)


    polynomial_parts = []
    for i, coeff in enumerate(sol.flatten()):
        if i == 0:
            polynomial_parts.append(f"{coeff}")
        else:
            polynomial_parts.append(f"({coeff:.2f})x^{i}")
    polynomial_str = " + ".join(polynomial_parts)


    result = sum(coeff * (x ** i) for i, coeff in enumerate(sol.flatten()))

    print(bcolors.OKGREEN, f"\nThe Result of P(X={x}) is:", bcolors.ENDC)
    print(result)
    return result






def calc_polinomial_guessian():

    table_points = [(1.2, -3.5), (1.3, -3.69), (1.4,0.9043), (1.5,1.1293), (1.6,2.3756)]
    x1 = 1.55
    x2 = 1.35


    polynomialInterpolation(table_points, x1)






if __name__ == '__main__':
    calc_polinomial_guessian()



