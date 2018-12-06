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
tr = 2 # tuned to get fastest possible rise time before saturation.
zeta = 0.8

kp = 3.05
kd = 7.2

#print('kp: ', kp)

#print('kd: ', kd)



