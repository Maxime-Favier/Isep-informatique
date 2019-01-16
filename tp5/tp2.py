def cube(x):
    return x**3

def volume(rayon):
    pi = 3.1416
    return float((4 / 3) * pi * cube(rayon))

print(volume(float(input("rayon \n"))))