# Boucle  while
nMax = 5
n = 1
a = []  # Create empty  l i s t
while n < nMax:
    a.append(1.0 / n)  # Append element to list
    # meme chose pour a.append(1/n) et a.append(1.0/ n)
    # [1, 0, 0, 0] pour a.append(1//n) => // = division euclidienne
    n += 1
print(a)

start = 1
stop = 5
step = 2
print("range(stop)=", range(stop))
print("range(start, stop)=", range(start, stop))
print("range(start, stop, step)=", range(start, stop, step))

nMax = 5
a = []  # Create empty  list
for n in range(1, nMax):
    a.append(1 / n)
print(a)
