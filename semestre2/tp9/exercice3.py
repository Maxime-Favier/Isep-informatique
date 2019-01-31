def pascal(hauteur):
    pascal = [[1], [1, 1]]

    for i in range(2, hauteur):
        pascal.append([1])
        for j in range(1, i):
            pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal[i].append(1)
    return pascal

def pprint(pascal):
    for i in pascal:
        print(i)

pprint(pascal(100))