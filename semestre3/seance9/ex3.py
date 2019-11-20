from numpy import array, linspace, cos, sin
from math import pi
from pylab import plot, xlabel, ylabel, title, show, axis, legend
from odes import ode23tx


def harmosc(y, t):
    ydot = array([y[1], -y[0]])
    return ydot


tspan = [0., 2 * pi]
y0 = array([1., 0.])
tout, yout = ode23tx(harmosc, tspan, y0)
n = 100
t = linspace(0, 2*pi, n)
yexact = array([cos(t), sin(t)])
yexact = yexact.T
plot(yout[:,0], yout[:,1], "-o")
plot(yexact[:,0], yexact[:,1], "-r")

axis('equal')
axis([-1.2, 1.4, -1.4, 1.6])
xlabel("y[0]")
ylabel("y[1]")
title("Diagramme de phase")
legend(("ode23tx", "Exact"))
show()