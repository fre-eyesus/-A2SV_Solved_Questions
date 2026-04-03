n = int(input())

parent = [int(input()) - 1 for _ in range(n - 1)]

leaf = [x for x in range(n) if x not in parent]

lp = [x for i, x in enumerate(parent) if i + 1 in leaf]

x = min(lp.count(k) for k in parent)

print("Yes" if x >= 3 else "No")