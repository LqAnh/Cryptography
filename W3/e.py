
import math


def m_e(x, e, p):
    return pow(x, e, mod=p)


x = 2
e = 173422142539
p = 727777887889889

#print(m_e(x, e, p))
#print((406130205920178 * 267367881434934) % 727777887889889)


def prime_factors(num):
    while num % 2 == 0:
        print(2,)
        num = num / 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            print(i,)
            num = num / i
    if num > 2:
        print(num)


num = 727777887889888
# prime_factors(num)
