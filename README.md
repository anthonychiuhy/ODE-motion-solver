# ODE-motion-solver
Solve equations of motion numerically for a particle in 2D experiencing a constant force acted towards or away from origin.

Circular motion is a special case in this problem setup where a = -r * omega^2 and v = r * omega

The solver employs the Runge-Kutta Method (RK4) in solving of the ODEs.

The resulted trajectory of the motion is plotted using matplotlib.
