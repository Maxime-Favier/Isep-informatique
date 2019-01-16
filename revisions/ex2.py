n = int(input('n? \n'))
fois = int(input('nbr de fois? \n'))
x= 0
for i in range(1, fois+1):
    x=x + n**i
    print(x)