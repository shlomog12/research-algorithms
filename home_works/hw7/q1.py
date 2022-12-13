
import cvxpy as cp
from cvxpy import log
import numpy as np
import matplotlib.pyplot as plt
import timeit
from utils import draw_graph_by_array


def generate_systems_of_linear_equations(n=None):
    max_range = 100000
    max_shape = 100
    if not n: 
        n = np.random.randint(1,max_shape)
    A = np.random.randint(-max_range,max_range, size=[n,n])
    B = np.random.randint(-max_range, max_range, size=[n,1])
    return A,B


def solve_by_cp(A,B):
    n = A.shape[0]
    X = cp.Variable(shape=(n,1))
    constraints = [A @ X == B]
    prob = cp.Problem(cp.Minimize(0) ,constraints)
    prob.solve()
    return X.value

A,B = generate_systems_of_linear_equations(10)
print(solve_by_cp(A,B))
print(np.linalg.solve(A, B))



def draw_graph_times_cp_vs_np(max_n=1000):
    times_cp = []
    times_np = []
    for i in range(max_n):
        A,B = generate_systems_of_linear_equations(i)
        time_of_cp = timeit.timeit(lambda: solve_by_cp(A,B),number=1)
        time_of_np = timeit.timeit(lambda: np.linalg.solve(A, B), number=1)
        times_cp.append(time_of_cp)
        times_np.append(time_of_np)
    

    label_X='iteration'
    label_Y='time'
    title_np = f"times of numpy--{max_n}"
    title_cp = f"times of cvxpy--{max_n}"

    draw_graph_by_array(times_np, title_np, label_X=label_X, label_Y=label_Y)
    draw_graph_by_array(times_cp, title_cp, label_X=label_X, label_Y=label_Y)


draw_graph_times_cp_vs_np(30)

