import itertools

p = 
a = 
b = 

xlable = dict()
ylable = dict()

# for all the number x, get the module (x^3 + ax + b) % p


def lablex(x):
    xlable.setdefault((x**3+a*x+b) % p, []).append(x)

# for all the number y, get the module (y^2) % p


def labley(y):
    ylable.setdefault((y**2) % p, []).append(y)


# calculate all the number
for num in range(0, p):
    lablex(num)
    labley(num)

# get all the points an length
intersect = []
for item in xlable.keys():
    if item in ylable:
        tmp = list(itertools.product(xlable[item], ylable[item]))
        intersect = intersect + tmp
print("points:", sorted(intersect))
print("+1 infinity point")
print("length:", len(intersect)+1)

