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

from numpy import linspace, pi, cos, sin, array
from numpy.linalg import norm
from pylab import plot, xlabel, ylabel, title, show, axis, legend
from odes import euler


def harmosc(y, t):
    ydot = array([y[1], -y[0]])
    return ydot


t0 = 0
tfinal = 2 * pi
y0 = array([1., 0.])
h = 0.1
t = t0
y = y0
while t <= tfinal:
    y = y + h * harmosc(y, t)
    t = t + h

print("y=", y)
yexact = [cos(tfinal), -sin(tfinal)]
print("yexact=", yexact)
print("nombre d'itération=", round(tfinal / h))
print("erreur absolue", abs(y[0] - yexact[0] + y[1] - yexact[1]))

tspan = [0., 2 * pi]
h = 0.1
y0 = [1., 0.]
tout, yout = euler(harmosc, tspan, y0, h)
n = 100
t = linspace(0, 2 * pi, n)
yexact = array([cos(t), sin(t)])
yexact = yexact.T
plot(yout[:, 0], yout[:, 1], "-o")
plot(yexact[:, 0], yexact[:, 1], "-r")

axis('equal')
axis([-1.2, 1.4, -1.4, 1.6])
xlabel("y[0]")
ylabel("y[1]")
title("Diagramme de phase")
legend(("Euler", "Exact"))
show()

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
t = linspace(0, 2 * pi, n)
yexact = array([cos(t), sin(t)])
yexact = yexact.T
plot(yout[:, 0], yout[:, 1], "-o")
plot(yexact[:, 0], yexact[:, 1], "-r")

axis('equal')
axis([-1.2, 1.4, -1.4, 1.6])
xlabel("y[0]")
ylabel("y[1]")
title("Diagramme de phase")
legend(("ode23tx", "Exact"))
show()

from numpy import array
from math import pi
from pylab import plot, xlabel, ylabel, title, show, axis
from odes import ode23tx

# def flame(y, t):
#    ydot = array([y ** 2 - y ** 3])
#    return ydot


# h = 0.01
# tspan = [0., 200.]
# tout, yout = ode23tx(flame, tspan, h)

# plot(yout[:, 0], yout[:, 1], "-o")
# xlabel("t (s)")
# ylabel("y")
# show()
