# Inverted Pendulum Parameter File
import numpy as np
# import control as cnt

# Physical parameters of the arm known to the controller
m = 5     # Mass of the arm, kg
ell = 0.3    # Length of the arm, m
g = 9.8       # Gravity, m/s**2
b = 0.5      # Damping coefficient, Nms
k = 3		# Spring constant

# parameters for animation
length = 5    # length of arm in animation
width = 0.3   # width of arm in animation

# Initial Conditions
theta0 = 0.0  # ,rads
thetadot0 = 0.0         # ,rads/s

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 50.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

# dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2.0*sigma-Ts)/(2.0*sigma+Ts)  # dirty derivative gain

# saturation limits
tau_max = 10                # Max torque, N-m

