import numpy as np
import matplotlib.pyplot as plt
from newton_method import results_newton as r_n

# ------------------input data--------------------
a = -3.00  # left border
b = 3.00  # right border
er = 1e-4  # optimal error


def func_1(x):
    return 2 * np.cos(x)


def func_2(x):
    return x ** 3 - np.sign(x) * x ** 2 + 6 * x + 3


# ------------------------------------------------------------
def find_matrix(func, left, right, node, error):
    grid_x = np.zeros((1, node))[0]
    grid_mid = np.zeros((1, node - 1))[0]  # grid middle node
    counter = node - 1
    for k in range(node):
        grid_x[counter] = (left + right) / 2 + (right - left) * np.cos(np.pi * (2 * k + 1) / (2 * node + 2)) / 2
        counter -= 1
    for j in range(node - 1):
        grid_mid[j] = round((grid_x[j + 1] - grid_x[j]) / 2 + grid_x[j], 6)
    grid = (np.array(grid_x), [0 for _ in range(node)])
    for j in range(node):
        grid[1][j] = func(grid_x[j]) + error
    mas_h = np.zeros((1, node - 1))[0]
    # grid = make_grid(func, left, right, node, error)
    for j in range(node - 1):
        mas_h[j] = grid[0][j + 1] - grid[0][j]
    # print('mas_h: ', np.round(mas_h, 2))
    delta = [error for _ in range(node)]
    matrix = np.zeros((node, node))
    matrix_g = np.zeros((1, node))[0]
    matrix_diagonal = np.ones((1, node))[0]
    for j in range(1, node - 1):
        matrix_diagonal[j] = (mas_h[j - 1] + mas_h[j]) / 3 + \
                             delta[j - 1] / (mas_h[j - 1] ** 2) + \
                             (((1 / mas_h[j - 1]) + (1 / mas_h[j])) ** 2) * delta[j] + \
                             delta[j + 1] / (mas_h[j] ** 2)
    matrix_diagonal = np.diag(matrix_diagonal)
    matrix[1, 0] = 1
    matrix[node - 1][node - 2] = 1
    for j in range(1, node - 2):
        matrix[j + 1][j] = mas_h[j] / 6 + (
                ((1 / mas_h[j - 1]) + (1 / mas_h[j])) * delta[j] + ((1 / mas_h[j - 1]) + (1 / mas_h[j])) * delta[
            j + 1]) / (-mas_h[j])
    for j in range(1, node - 3):
        matrix[j + 2][j] = delta[j + 1] / (mas_h[j] * mas_h[j + 1])
    for j in range(1, node - 1):
        matrix_g[j] = (grid[1][j + 1] - grid[1][j]) / mas_h[j] - (grid[1][j] - grid[1][j - 1]) / mas_h[j - 1]
    matrix = matrix + matrix_diagonal + np.transpose(matrix)
    inv_matrix = np.array(np.linalg.inv(matrix))
    matrix_n = inv_matrix.dot(np.array(matrix_g))
    matrix_d = np.zeros((1, node))[0]
    matrix_d[0] = (matrix_n[1] - matrix_n[0]) / mas_h[0]
    for j in range(1, node - 1):
        matrix_d[j] = (matrix_n[j + 1] - matrix_n[j]) / mas_h[j] - (matrix_n[j] - matrix_n[j - 1]) / mas_h[j - 1]
    matrix_d[node - 1] = - (matrix_n[node - 1] - matrix_n[node - 2]) / mas_h[node - 2]
    matrix_z = np.zeros((1, node))[0]
    for j in range(node):
        matrix_z[j] = grid[1][j] - delta[j] * matrix_d[j]

# ------------------------------------------------end method------------------------------------------------------------

    def create_delta():
        delta_x = np.zeros((1, 5 * (node - 1)))[0]
        count = 0
        for j in range(node - 1):
            r = grid_x[j + 1] - grid_x[j]
            for k in range(5):
                delta_x[count] = k * r / 5 + grid_x[j]
                count += 1
        return delta_x

    def find_result(delt):
        matrix_t = np.zeros((1, 5 * (node - 1)))[0]
        count_1 = 0
        for j in range(node - 1):
            for k in range(5):
                matrix_t[count_1] = (delt[count_1] - grid_x[j]) / mas_h[j]
                count_1 += 1
        mas_y = np.zeros((1, 5 * (node - 1)))[0]
        count_2 = 0
        for j in range(node - 1):
            for k in range(5):
                mas_y[count_2] = matrix_z[j] * (1 - matrix_t[count_2]) + matrix_z[j + 1] * matrix_t[count_2] - matrix_t[
                    count_2] * (1 - matrix_t[count_2]) * (
                                             (2 - matrix_t[count_2]) * matrix_n[j] + (1 + matrix_t[count_2]) * matrix_n[
                                         j + 1]) * (
                                         mas_h[j] ** 2) / 6
                count_2 += 1
        return mas_y

    res = create_delta()
    final_mas = find_result(create_delta())

    def find_abs_error():
        abs_error = np.zeros((1, node - 1))[0]
        for j in range(node - 1):
            abs_error[j] = func(grid_mid[j]) - final_mas[j * 5 - 2]
        return abs_error

    final_abs_error = max(find_abs_error())

