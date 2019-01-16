import statistics

x = 0
list = []
while x != -1:
    x = int(input())
    if x != -1:
        list.append(x)
        # print(list)

print(min(list), "minimum")
print(max(list), "maximum")
print(statistics.mean(list), "moyenne")