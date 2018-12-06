# Single link arm Parameter File
import numpy as np
# import control as cnt
import sys
sys.path.append('..')  # add parent directory
import armParam as P

Ts = P.Ts  # sample rate of the controller
beta = P.beta  # dirty derivative gain
tau_max = P.tau_max  # limit on control signal

#  tuning parameters
#tr = 0.8 # part (a)
tr = 2  # tuned to get fastest possible rise time before saturation.
zeta = 0.7
ki = 1.5  # integrator gain

# desired natural frequency
wn = 2.2 / tr
alpha1 = 2.0*zeta*wn
alpha0 = wn**2

# compute PD gains
#kp = alpha0*(P.m*P.ell**2)/3.0
#kd = (P.m*P.ell**2)/3.0*(alpha1m -3.0*P.b/(P.m*P.ell**2))

kp = 3.05
kd = 7.2

print('kp: ', kp)
print('ki: ', ki)
print('kd: ', kd)



