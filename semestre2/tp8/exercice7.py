T = [2, 65, 42, 53, 27, 2, 42, 27, 2, 53, 53, 53, 65, 21, 27, 53, 2, 53, 65, 27]
n = len(T)

for j in range(0, len(T) - 1):
    indiceMin = j
    for k in range(j + 1, len(T)):
        if T[k] < T[indiceMin]:
            indiceMin = k
    if indiceMin != j:
        T[j], T[indiceMin] = T[indiceMin], T[j]

print(T)
