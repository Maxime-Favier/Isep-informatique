# -*- coding: utf-8 -*-
x = 1

while x == 1:
    a = int(input("a"))
    b = int(input("b"))
    op = input("operation")
    if b == 0 and op == "/":
        print("division par 0")
    else:
        print(eval(str(a) + op + str(b)))
    x = int(input("continuez ? O/1"))