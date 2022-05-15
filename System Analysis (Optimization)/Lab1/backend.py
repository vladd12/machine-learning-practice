import numpy as np
from scipy.optimize import linprog


def scipy_algo(in_a, in_b, in_c):
    a = np.array(in_a)
    b = np.array(in_b)
    c = np.array(in_c)
    print("\nРешение SciPy")
    print("Input:\n", a, '\n', b, '\n', c)
    x0_bounds = (0, None)
    x1_bounds = (0, None)
    res = linprog(c * -1, A_ub=a, b_ub=b,
                  bounds=[x0_bounds, x1_bounds],
                  method='simplex')
    print("Решение:", res.x)
    print("Максимальное значение:", res.fun * -1)
    return res.x, res.fun * -1


def my_algo(in_a, in_b, in_c):
    a = np.array(in_a)
    b = np.array(in_b)
    c = np.array(in_c)
    print("\nМоё решение")
    print("Input:\n", a, '\n', b, '\n', c)
    matrix = np.array([
        np.append(c * -1, [0, 0, 0, 0]),
        np.append(a[0], [1, 0, 0, b[0]]),
        np.append(a[1], [0, 1, 0, b[1]]),
        np.append(a[2], [0, 0, 1, b[2]])
        ], dtype=float)
    
    while (matrix[0].min() < 0):
        i_col = matrix[0].argmin()
        permission_column = matrix[:, i_col]
        i_row = (matrix[:, 5] / permission_column)[1:].argmin() + 1
        matrix[i_row] = matrix[i_row]/ matrix[i_row, i_col]
        for i in range(0, matrix.shape[0]):
            if (i != i_row):
               matrix[i] = matrix[i] - matrix[i, i_col] * matrix[i_row]
    
    for i in reversed(range(0, 4)):
        if (matrix[0, i] != 0.0):
            matrix = np.delete(matrix, i, axis=1)
            
    last_col = matrix[:, len(matrix[0]) - 1]
    x1 = float(last_col[np.where(matrix[:, 0] == 1)])
    x2 = float(last_col[np.where(matrix[:, 1] == 1)])
    res = matrix[0, len(matrix[0]) - 1]
    print("Решение:", [x1, x2])
    print("Максимальное значение:", res)
    return [x1, x2], res


if (__name__ == "__main__"):
    print("Задача максимизации")
    a = [[3, 6], [4, 3], [5, 2]]
    b = [102, 91, 105]
    c = [7, 9]
    scipy_algo(a, b, c)
    my_algo(a, b, c)

