n , k = map(int, input().split())

seg = list(map(int,input().split()))

from collections import Counter

count = Counter()

l= 0
good = 0
for r in range(n):
    count[seg[r]] += 1

    while len(count) > k:
        count[seg[l]] -= 1
        
        if count[seg[l]] == 0:
            del count[seg[l]]
        
        l += 1

    
    good += (r - l + 1)

print(good)


