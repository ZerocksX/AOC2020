from __future__ import print_function
inp = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

inp = """Player 1:
41
33
20
32
7
45
2
12
14
29
49
37
6
11
39
46
47
38
23
22
28
10
36
35
24

Player 2:
17
4
44
9
27
18
30
42
21
26
16
48
8
15
34
50
19
43
25
1
13
31
3
5
40
"""

lines = inp.split("\n")

decks = []
deck = []
for line in lines:
    if line == "":
        decks.append(deck)
        deck = []
    elif line[0] == 'P':
        continue
    else:
        deck.append(int(line))
print(decks)

while len(decks[0]) != 0 and len(decks[1]) != 0:
    d1 = decks[0]
    d2 = decks[1]
    t1 = d1[0]
    t2 = d2[0]
    d1.pop(0)
    d2.pop(0)
    if t1 > t2:
        d1.append(t1)
        d1.append(t2)
    else:
        d2.append(t2)
        d2.append(t1)
d = decks[0] if len(decks[0]) != 0 else decks[1]
res = 0
for i in range(1, len(d) + 1):
    res += i * d[-i]
print(res)