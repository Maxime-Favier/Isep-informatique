def la_meilleure_ville0(villes, n, lignes, m, gares, g):
    pass
(n, m, g) = list(map(int, input().split()))
villes = [None] * n
for i in range(0, n):
    villes[i] = int(input())
lignes = [None] * m
for j in range(0, m):
    (depart, arrivee, temps) = list(map(int, input().split()))
    trajet = {"depart":depart, "arrivee":arrivee, "temps":temps}
    lignes[j] = trajet
gares = [None] * g
for k in range(0, g):
    (dep, arr, tmp) = list(map(int, input().split()))
    traj = {"depart":dep, "arrivee":arr, "temps":tmp}
    gares[k] = traj
la_meilleure_ville0(villes, n, lignes, m, gares, g)