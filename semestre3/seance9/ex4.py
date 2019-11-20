from numpy import array
from math import pi
from pylab import plot, xlabel, ylabel, title, show, axis
from odes import ode23tx


def flame(y, t):
    ydot = array([y ** 2 - y ** 3])
    return ydot


h = 0.01
tspan = [0., 200.]
tout, yout = ode23tx(flame, tspan, h)

plot(yout[:, 0], yout[:, 1], "-o")
xlabel("t (s)")
ylabel("y")
show()
