test = int(input())

for _ in range(test):
    n, k = map(int, input().split())
    casino = [list(map(int, input().split())) for _ in range(n)]
    
    casino.sort(key=lambda x: x[0])

    for a, b, c in casino:
        if a <= k:
            k = max(k, c)
        else:
            break

    print(k)
