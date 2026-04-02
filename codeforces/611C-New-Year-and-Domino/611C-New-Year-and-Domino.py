def get(ps, r1, c1, r2, c2):
    return ps[r2][c2] - ps[r1-1][c2] - ps[r2][c1-1] + ps[r1-1][c1-1]

q = int(input())

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    res = 0

    if c1 < c2:
        res += get(ph, r1, c1, r2, c2-1)

    if r1 < r2:
        res += get(pv, r1, c1, r2-1, c2)

    print(res)