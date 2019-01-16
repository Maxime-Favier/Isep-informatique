x = 42

for i in range(1, 333):
    x = (1337 * x + 404) % 1000
print(x)