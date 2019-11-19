## 1. La fonction  sys .float_info
print("")
print(" 1. La fonction sys.float_info")
import sys

print(sys.float_info)
print("max: ", sys.float_info.max)
print("max_exp : ", sys.float_info.max_exp)
print("min : ", sys.float_info.min)
print("min_exp : ", sys.float_info.min_exp)
print("mant_dig : ", sys.float_info.mant_dig)
print("epsilon : ", sys.float_info.epsilon)

## 2. Nombre extremes
print("")
print("2. Nombre extremes")
print(" 1. e1000=", 1.e1000)  # overflow
print("−1.e1000=", -1.e1000)  # underflow
print(" 1. e−1000=", 1.e-1000)  # underflow
print("−1.e−1000=", -1.e-1000)  # overflow

# 3.  Epsilon  machine
# a) 53 de sys.float_info.mant_dig
print("")
print(" 3. Epsilon machine")
eps = 1.0
n = 1
while 1 + eps > 1:
    eps = eps / 2.0
    print("n=", n, " ,eps=", eps)
    n = n + 1
# b) elle s'arrette quand 1 + eps > 1
# c) n= 53  ,eps= 1.1102230246251565e-16
# d) 53 itérations
