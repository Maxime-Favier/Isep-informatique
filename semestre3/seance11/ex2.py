from numpy import array, transpose, dot, linspace, vander, set_printoptions, arange
from numpy.linalg import qr, solve, norm, cond
from pylab import plot, title, show, xlabel, ylabel, savefig, grid, yticks
from leastsq import polyfit, polyval
from math import log10

t = array([1900., 1910., 1920., 1930., 1940., 1950., 1960., 1970., 1980., 1990., 2000])
y = array([76., 92., 106., 123., 132., 151., 179., 203., 227., 250., 281.])
#t = array([0.,1.,2.,3.,4.,5.,6.])
#y =array([0., 1., 3.,6.,9.,11.,12.])
n = 3
X = vander(t, n)
Q, R = qr(X)
print("log10(cond(R))=", log10(cond(R)))
z = dot(transpose(Q), y)
bet = solve(R, z)
print("beta=", bet)

bet = polyfit(t, y, n)
u = linspace(1890, 2020, 100)
#u = arange(0, 6.1, 0.1)
v = polyval(bet, u)
plot(t, y, "o")
plot(u, v, "-")
xlabel("Durée de la marée (/HM)")
ylabel("Marnage (dz)")
#yticks(list(range(0, 13)))
#grid()
savefig("maree.png")
show()

bet = polyfit(t, y, n)
v = polyval(bet, [2020.])
print("Prediction 2010", v)

