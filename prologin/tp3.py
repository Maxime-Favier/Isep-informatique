from collections import Counter


# import random

def manhattan_maboul0(m, jours, n):
    maximum = 0
    count = Counter(jours)
    # commence un jour ou qqun arrive + supprime les doublets
    for arrive in count.keys():
        temp = 0
        for i in range(arrive, arrive + m + 1):
            # print(i)
            temp += count[i]
        # print("end", temp)
        if temp > maximum:
            maximum = temp
    print(maximum)


(n, m) = list(map(int, input().split()))
jours = list(map(int, input().split()))
# x= [random.randrange(1,1000000) for _ in range(0,1000000)]
# l = len(x)
manhattan_maboul0(m, jours, n)
