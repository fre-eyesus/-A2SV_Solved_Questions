n,k = map(int,input().split())

seg = list(map(int,input().split()))

from collections import Counter

count = Counter()

ans = [0]* 2
mx_len = 0
l = 0
for r in range(n):
    count[seg[r]] += 1

    while len(count) > k:
        count[seg[l]] -= 1

        if count[seg[l]] == 0:
            del count[seg[l]]
        l += 1
    
    if len(count) <= k:
        ln = r - l + 1

        if ln > mx_len:
            ans[0] = l + 1
            ans[-1] = r + 1
        mx_len = max(ln, mx_len)
    
print(*ans)


    
