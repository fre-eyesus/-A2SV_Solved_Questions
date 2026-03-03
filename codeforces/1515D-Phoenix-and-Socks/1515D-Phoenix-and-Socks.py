from collections import Counter

t = int(input())

for _ in range(t):
    n, L, R = map(int, input().split())
    colors = list(map(int, input().split()))
    
    left = Counter(colors[:L])
    right = Counter(colors[L:])
    
    for c in list(left.keys()):
        m = min(left[c], right[c])
        left[c] -= m
        right[c] -= m
        L -= m
        R -= m
    
    if L < R:
        left, right = right, left
        L, R = R, L
    
    ans = 0
    
    diff = L - R
    
    for c in left:
        if diff <= 0:
            break
        pairs = left[c] // 2
        use = min(pairs * 2, diff)
        ans += use // 2
        left[c] -= use
        L -= use
        diff -= use
    
    ans += (L - R) // 2
    ans += (L + R) // 2
    
    print(ans)