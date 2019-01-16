for i in range(0, 11):
    if i < 5:
        print(" " * (i+1), "*", " " * (9 - i * 2), "*", sep="")
    elif i == 5:
        print(" " * 5, "*")
    else:
        print(" " * (11 - i), "*", " " * (i-(11-i)), "*", sep="")
