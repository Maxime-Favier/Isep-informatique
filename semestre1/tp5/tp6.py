def age(a):
    if a <=2:
        return 10.5*a
    else:
        return (10.5*2) + (4* (a-2))


print(age(int(input("age"))))