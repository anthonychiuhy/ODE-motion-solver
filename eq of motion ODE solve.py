# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 02:09:53 2019

@author: Anthony Chiu

Solves differential equations of motion for constant acceleration in the direction of r in 2D polor coordinates (r(t), theta(t)) using RK4

Equations of motion:
dr = x
dx = k2 + k1^2/r^3
dtheta = k1/r^2

Let F = (r, x, theta)
   dF = (dr, dx, dtheta)
     
Solve for DF = f(F)

"""
import numpy as np
import matplotlib.pyplot as plt

# Define initial position and speed
r0 = 4 # initial r
x0 = -5 # initial speed in r
theta0 = 0 # initial theta
F0 = np.array([r0, x0, theta0])

# Define problem constants
k1 = 16 # k1 = dtheta0 * r0^2 
k2 = -4 # acceleration in direction of r
K = np.array([k1, k2])

# Define step size and time frame
step = 0.01
t0 = 0
tf = 40
T = np.arange(t0, tf, step)

F = np.zeros([F0.shape[0], T.shape[0]])
F[:, 0] = F0

# Define dF = f(F)
def dF(F):
    return np.array([F[1], K[1] + K[0]**2/F[0]**3, K[0]/F[0]**2])

# Solve using RK4
for i in range(len(T) - 1):
    A1 = step * dF(F[:, i])
    A2 = step * dF(F[:, i] + A1/2)
    A3 = step * dF(F[:, i] + A2/2)
    A4 = step * dF(F[:, i] + A3)
    F[:, i+1] = F[:, i] + 1/6 * (A1 + 2*A2 + 2*A3 + A4)

#  Plot everything
XY = np.zeros((F.shape[0] - 1, F.shape[1]))
# convert position in (x, y)
XY[0, :] = F[0, :] * np.cos(F[2, :])
XY[1, :] = F[0, :] * np.sin(F[2, :])
# plot final position and origin
plt.plot(XY[0, -1], XY[1, -1], 'ro')
plt.plot(0, 0, 'r+')
plt.axis([-10, 10, -10, 10])
plt.ylabel('y')
plt.xlabel('x')
# plot results
plt.plot(XY[0, :], XY[1, :])

# Sanity check
print('Number of r < 0 =', np.sum(F[0, :] < 0))