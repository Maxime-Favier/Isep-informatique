import random


def ranking(entree):
    # t = sorted(entree)
    # out = [t.index(v) for v in entree]
    out = [0] * len(entree)
    for i, x in enumerate(sorted(range(len(entree)), key=lambda y: entree[y])):
        out[x] = i
    return out


def statuettes0(motif, n, tailles, m):
    occurences = []
    # conversion du motif
    out = [0] * n
    for i, el in enumerate(motif):
        # print(i, el)
        out[el - 1] = i
    # verification des tailles
    for j in range(0, m - n + 1):
        ta = tailles[j:j + n]
        for i in range(n - 1):
            # print(i, ta)
            if (out[i] < out[i + 1] and ta[i] < ta[i + 1]) or (out[i] > out[i + 1] and ta[i] > ta[i + 1]):
                # motif montant ou descendant le meme que pour les tailles pour les eliminer plus vite
                # la fonction ranking premant trop de temps
                # print("vrai", motif[i], motif[i + 1], ta[i], ta[i + 1])
                if i == n - 2:
                    # verification complémentaires classique
                    rank = ranking(ta)
                    if rank == out:
                        occurences.append(j + 1)
                    break
            else:
                break

    print(len(occurences))
    print(str(occurences).replace(",", "").replace("[", "").replace("]", ""))


# (n, m) = list(map(int, input().split()))
# motif = list(map(int, input().split()))
# tailles = list(map(int, input().split()))
# statuettes0(motif, n, tailles, m)
motif = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tailles = [random.randrange(1, 20) for _ in range(0, 100000000)]
print("done")
statuettes0(motif, len(motif), tailles, len(tailles))
