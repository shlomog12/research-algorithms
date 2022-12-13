
import cvxpy as cp
from cvxpy import log
import numpy as np
import matplotlib.pyplot as plt
import timeit


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

def drow_graph_by_array(arr, title):
    path = './hw7/Q1/'
    plt.title(title)
    plt.xlabel('iteration')
    plt.ylabel('time')
    plt.plot(range(len(arr)), arr, color="blue")
    plt.savefig(f'{path}{title}.png')
    plt.close()


def drow_graph_times_cp_vs_np(max_n=1000):
    times_cp = []
    times_np = []
    for i in range(max_n):
        A,B = generate_systems_of_linear_equations(i)
        time_of_cp = timeit.timeit(lambda: solve_by_cp(A,B),number=1)
        time_of_np = timeit.timeit(lambda: np.linalg.solve(A, B), number=1)
        times_cp.append(time_of_cp)
        times_np.append(time_of_np)
    
    drow_graph_by_array(times_np,f"times of numpy--{max_n}")
    drow_graph_by_array(times_cp,f"times of cvxpy--{max_n}")

    # print('numpy:\n\n\n\n\n\n\n')
    # print(times_np)
    # print('\n\n\n\n\n\n\n\n')
    # print('cp:\n\n\n\n\n\n\n')
    # print(times_cp)

drow_graph_times_cp_vs_np(30)

