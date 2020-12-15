inp = """0,3,6"""
inp = "1,3,2"
inp = "2,1,3"
inp = "1,2,3"
inp = "12,1,16,3,11,0"
nums = [int(a) for a in inp.split(",")]
from collections import defaultdict

d = defaultdict(list)

for i, num in enumerate(nums):
    d[num] = [i + 1] + d[num] 

last_num = nums[-1]
for i in range(len(nums) + 1, 30000000+1):
    if i % 1000000 == 0:
        print(i)
    if len(d[last_num]) < 2:
        d[0] = [i, d[0][0]]
        last_num = 0
    else:
        diff = d[last_num][0] - d[last_num][1]
        if len(d[diff]):
            d[diff] = [i, d[diff][0]]
        else:
            d[diff] = [i]
        last_num = diff
print(last_num)
#print(d)
#print(nums)