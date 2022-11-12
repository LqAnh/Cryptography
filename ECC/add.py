# eg: P = [1, 2]
#     Q = [3, 4] if you want to add P to itself then Q = P
#     num : number of time you want to calculate P start from 2
#         -  eg: calculate 2P => num = 3
#         -  P + Q => num = 3
#         -  3P => num = 4
#         -  4P => num = 5
#     prime, a, b: y^2 = x^3 + ax + b mod prime
P = [0, 1023]
Q = P
num = 3217
prime = 3121
a = 13
b = 994


def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def sign(x):
    return 1 if x >= 0 else -1


def gcdExtendedGeneralized(a, b):
    gcd, x1, y1 = gcdExtended(abs(a), b)
    return gcd, (sign(a) * x1) % b, y1 % b


def double_point(point: list):
    x = point[0]
    y = point[1]

    s = ((3*(x**2)+a) * (gcdExtendedGeneralized(2*y, prime)[1])) % prime

    newx = (s**2 - x - x) % prime
    newy = (s * (x - newx) - y) % prime

    return [newx, newy]


def add_points(P: list, Q: list):
    x1 = P[0]
    y1 = P[1]
    x2 = Q[0]
    y2 = Q[1]

    s = ((y2 - y1) *
         ((gcdExtendedGeneralized(x2-x1, prime))[1] % prime)) % prime

    newx = (s**2 - x1 - x2) % prime
    newy = (s * (x1 - newx) - y1) % prime

    return [newx, newy]


index = 2
while True:
    if Q[0] == P[0] and Q[1] == P[1]:
        # print("doubling")
        Q = double_point(P)
    else:
        # print("adding")
        Q = add_points(P, Q)

    if index == num:
        break

    print(f"{index}P = {Q}")
    index += 1
