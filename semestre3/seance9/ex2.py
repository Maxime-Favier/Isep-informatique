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
    y = y + h*harmosc(y, t)
    t = t+ h

print("y=", y)
yexact = [cos(tfinal), -sin(tfinal)]
print("yexact=", yexact)
print("nombre d'itération=", round(tfinal/h))
print("erreur absolue", abs(y[0]-yexact[0]+y[1]-yexact[1]))

tspan = [0., 2*pi]
h = 0.1
y0 = [1., 0.]
tout, yout = euler(harmosc, tspan, y0, h)
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
legend(("Euler", "Exact"))
show()