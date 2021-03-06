inp = """939
7,13,x,x,59,x,31,19"""
inp = """1001287
13,x,x,x,x,x,x,37,x,x,x,x,x,461,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,739,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,23"""

lines = inp.split("\n")
t = int(lines[0])
busss = [ (i, int(x)) for i,x in enumerate(lines[1].split(",")) if x != 'x' ]
buss = [ int(x) for x in lines[1].split(",") if x != 'x' ]
print(t, buss)
times = [(((t // x) + 1) * x)  for x in buss]
ret = [(i, x - t) for i, x in enumerate(times)]
ret = min(ret, key = lambda x: x[1])

print(ret[1] * buss[ret[0]])


for i,b in busss:
    print("x congruent to %d (mod %d)"  % (-i, b))

# Part 2 chinese remainder theory
# Online solver

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

n = [b for i,b in busss]
a = [-i for i,b in busss]

print (chinese_remainder(n, a))
