from scipy.integrate import odeint
from numpy import linspace, pi, sqrt, array
from numpy.linalg import eig
from pylab import plot, xlabel, ylabel, title, show, axis, grid
from odes import odeplot


def harmosc(y, t):
    ydot = [y[1], -y[0]]
    return ydot


y0 = [1, 0]
t = linspace(0, 2 * pi, 100)
y = odeint(harmosc, y0, t)
plot(y[:, 0], y[:, 1], "-o")
title("Harmonic oscillator : phase plot")
axis('equal')
axis([-1.2, 1.2, -1.2, 1.2])
xlabel("y[0]")
ylabel("y[1]")
show()

odeplot(t, y, "oscillateur harmonique", "-")