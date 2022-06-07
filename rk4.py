import math
import matplotlib.pyplot as plt

# Constants
T_0 = 0
Y_0 = 1

T_FINAL = 5
DT = 0.5
DT_EXACT = 0.01


# Functions
def f(t, y):
    return math.sin(t)**2 * y

def euler_step(t_i, y_i, dt, f):
    return y_i + dt*f(t_i, y_i)

def rk4_step(t_i, y_i, dt, f):
    k1 = f(t_i, y_i)
    k2 = f(t_i + dt/2, y_i + k1*dt/2)
    k3 = f(t_i + dt/2, y_i + k2*dt/2)
    k4 = f(t_i + dt, y_i + k3*dt)
    return y_i + dt/6*(k1 + 2*k2 + 2*k3 + k4)

def y_exact(t_0, y_0, t):
    exp_arg = 1/2 * ( (t-t_0) - (math.sin(t)*math.cos(t) - math.sin(t_0)*math.cos(t_0)) )
    return y_0*math.exp(exp_arg)


# Computing exact result
t = T_0

ys_exact = []
ts_exact = []

while t < T_FINAL:
    ts_exact.append(t)
    ys_exact.append(y_exact(T_0, Y_0, t))
    t += DT_EXACT


# Computing approximate results
ts = [T_0]
ys = [Y_0]
ys_euler = [Y_0]

y = Y_0
y_euler = Y_0
t = T_0

while t < T_FINAL:
    # Solving with Runge-Kutta
    y = rk4_step(t, y, DT, f)

    # Solving with Euler
    y_euler = euler_step(t, y_euler, DT, f)

    # Increasing t
    t += DT

    # Appending results
    ts.append(t)
    ys.append(y)
    ys_euler.append(y_euler)


# Plotting
plt.plot(ts, ys, color='red', marker='o', linewidth=0.0, label='RK4')
plt.plot(ts, ys_euler, color='green', marker='o', linewidth=0.0, label='Euler')
plt.plot(ts_exact, ys_exact, color='blue', label='Exact')
plt.legend()
plt.show()





























































