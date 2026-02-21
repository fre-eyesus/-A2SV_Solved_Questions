n = int(input())
points = list(map(int, input().split()))

points.sort()

mid = 0

if n % 2 == 1:
    mid = points[n//2 ]
else:
    mid = points[n//2 - 1]

print(mid)
