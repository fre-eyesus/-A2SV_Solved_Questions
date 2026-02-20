contest = int(input())
problems = list(map(int, input().split()))

problems.sort()

days = 0
incr = 1
for p in problems:
    if p >= incr:
        days += 1
        incr+= 1
  

print(days)
