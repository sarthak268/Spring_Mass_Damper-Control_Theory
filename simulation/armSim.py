import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')  # add parent directory
import armParam as P
from signalGenerator import signalGenerator
from armAnimation import armAnimation
#from plotData import plotData
from slider_input import *

# instantiate reference input classes
reference = signalGenerator(amplitude=0.5, frequency=0.1)
#thetaRef = signalGenerator(amplitude=0.2*np.pi, frequency=0.1)
tauRef = signalGenerator(amplitude=5, frequency=.5)

# instantiate the simulation plots and animation
#dataPlot = plotData()
animation = armAnimation()

t = P.t_start  # time starts at t_start
obj = mySlider()
while t < P.t_end:  # main simulation loop
    # set variables
    r = reference.square(t)
    #theta = thetaRef.sin(t)
    theta = obj.getValue()
    print(theta)
    obj.update(theta)
    tau = tauRef.sawtooth(t)
    # update animation
    state = [theta, 0.0]
    animation.drawArm(state)
    #dataPlot.updatePlots(t, r, state, tau)

    t = t + P.t_plot  # advance time by t_plot
    plt.pause(0.5)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
