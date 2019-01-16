def max2(x, y):
    if x > y:
        return x
    else:
        return y


def max3(x, y, z):
    if x > y:
        return max2(x, z)
    else:
        return max2(y, z)


print(max3(int(input("1er nbr \n")), int(input("2eme nbr \n")), int(input("3em nbr \n"))))
