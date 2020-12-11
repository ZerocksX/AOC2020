input = """16
10
15
5
1
11
7
19
6
12
4"""
input = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
input = """73
114
100
122
10
141
89
70
134
2
116
30
123
81
104
42
142
26
15
92
56
60
3
151
11
129
167
76
18
78
32
110
8
119
164
143
87
4
9
107
130
19
52
84
55
69
71
83
165
72
156
41
40
1
61
158
27
31
155
25
93
166
59
108
98
149
124
65
77
88
46
14
64
39
140
95
113
54
66
137
101
22
82
21
131
109
45
150
94
36
20
33
49
146
157
99
7
53
161
115
127
152
128"""
lines = input.split("\n")
nums = []
for line in lines:
    nums.append(int(line))
nums = list(sorted(nums))
print(nums)

ones, threes = 0, 1
jolt = 0
for num in nums:
    if num - jolt == 1:
        ones += 1
    elif num - jolt == 3:
        threes += 1
    jolt = num
print(ones*threes)


dp = [0 for i in range(max(nums) + 1)]
dp[0] = 1

for num in nums:
    for i,k in enumerate(dp):
        if num - 3 <= i and num > i:
            dp[num] += dp[i]
print(dp[-1])