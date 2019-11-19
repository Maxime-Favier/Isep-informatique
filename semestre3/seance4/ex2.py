from pylab import plot, yscale, show, title, xlabel, ylabel
from numpy import log, linspace
from floats import logCond

print("log(1.01)", log(1.01), "logCond(1.01)", logCond(1.01))
print("log(1.0001)", log(1.0001), "logCond(1.0001)", logCond(1.0001))
print("log(1.000001)", log(1.000001), "logCond(1.000001)", logCond(1.000001))

x = linspace(0.5, 1.5, 1000)
y = log(x)
c = logCond(x)
title("log")
plot(x, y, "r-")
xlabel("x")
ylabel("log(x)")
show()

title("Condition number of log")
plot(x, c, "r-")
yscale("log")
xlabel("x")
ylabel("Condition-Log(x)")
show()