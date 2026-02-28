t = int(input())

for _ in range(t):
    n, k = map(int,input().split())

    letter = input()

    from collections import defaultdict
    count = defaultdict(int)
    
    op = 2 *(10 ** 5) + 1
    l = 0
    found = False
    for r in range(n):
        count[letter[r]] += 1

        while sum(count.values()) > k:
            count[letter[l]] -= 1

            l += 1
        if sum(count.values()) == k:
            found = True
            op = min(op,count["W"])
        
    print(op) if found else print(0)
