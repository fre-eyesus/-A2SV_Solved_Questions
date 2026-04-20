def f(a, l, r):
    if r - l == 1:
        return 0
    m = (l + r) // 2
    x = max(a[l:m])
    y = max(a[m:r])
    c = 0
    if x > y:
        c = 1
        for i in range(m - l):
            a[l + i], a[m + i] = a[m + i], a[l + i]
    return f(a, l, m) + f(a, m, r) + c

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = f(a, 0, n)
    if a == sorted(a):
        print(ans)
    else:
        print(-1)