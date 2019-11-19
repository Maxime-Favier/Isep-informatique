# Listes
a = [1.0, 2.0, 3.0]  # Create a  l i s t
print("a=", a)
for i, j in enumerate(a):
    print("a[" + str(i) + "] =", j)

print(" len(a)=", len(a))  # Determine  length  of  l i s t
a[1: 3] = [12.0, 13.0]
print(" len(a)=", len(a))
