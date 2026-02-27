n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


ans = 0
from collections import Counter
count_a = Counter(a)
count_b = Counter(b)

both = []
both.extend(a)
both.extend(b)


for el in set(both):
    if el in count_a and el in count_b:
        ans += count_a[el] * count_b[el]

print(ans)
