import numpy as np
import matplotlib.pyplot as plt
from numbalsoda import lsoda_sig, lsoda
from numba import cfunc

# Function to calculate decay rate
def decay(T):
    return np.log(2) / T

# Define decay rates
x1_decay = decay(186)
x2_decay = decay(1610)
x4_decay = decay(1194)
x7_decay = decay(1.643e-4)
x9_decay = decay(7.01e8)
x11_decay = decay(5.99e26)
x14_decay = decay(7.01e8)
x16_decay = decay(252.12)

# Define transition probabilities
p21 = 1 - 0.02 / 100
p42 = 1
p74 = 1 - 0.021 / 100 - 0.003 / 100
p97 = 1
p119 = 1 - 1.9e-6 / 100
p1411 = 1

# Define the ODE right-hand side function
@cfunc(lsoda_sig)
def rhs(t, y, dy, p):
    x1, x2, x4, x7, x9, x11, x14, x16 = (y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7])

    dy[0] = -x1_decay * x1
    dy[1] = x1_decay * x1 * p21 - x2_decay * x2
    dy[2] = x2_decay * x2 * p42 - x4_decay * x4
    dy[3] = x4_decay * x4 * p74 - x7_decay * x7
    dy[4] = x7_decay * x7 * p97 - x9_decay * x9
    dy[5] = x9_decay * x9 * p119 - x11_decay * x11
    dy[6] = x11_decay * x11 * p1411 - x14_decay * x14
    dy[7] = x14_decay * x14

# Function to simulate the ODE
def simulate_ode():
    funcptr = rhs.address  # Address to the ODE function
    initial_conditions = np.array([1e5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    data = np.array([1.0])  # Data you want to pass to rhs
    t_eval = np.linspace(0.0, 20000, 100000)  # Times to evaluate the solution

    solution, success = lsoda(funcptr, initial_conditions, t_eval, data=data)

    return solution, t_eval

# Function to plot the results
def plot_results(solution, t_eval):
    x1 = solution[:, 0]
    x2 = solution[:, 1]
    x4 = solution[:, 2]
    x7 = solution[:, 3]
    x9 = solution[:, 4]
    x11 = solution[:, 5]
    x14 = solution[:, 6]
    x16 = solution[:, 7]

    # Create a time array based on t_eval
    time = t_eval

    # Plot each variable
    plt.figure(figsize=(10, 6))
    plt.plot(time, x1, label='x1')
    plt.plot(time, x2, label='x2')
    plt.plot(time, x4, label='x4')
    plt.plot(time, x7, label='x7')
    plt.plot(time, x9, label='x9')
    plt.plot(time, x11, label='x11')
    plt.plot(time, x14, label='x14')
    plt.plot(time, x16, label='x16')

    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.title('ODE Simulation Results')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    solution, t_eval = simulate_ode()
    plot_results(solution, t_eval)
