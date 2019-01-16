nbr = input('nbr')
out =""
for i in range(len(nbr), 0, -1):
    out = out + nbr[i-1]
    # print(i)
print(out)