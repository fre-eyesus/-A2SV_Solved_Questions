t = int(input())
for _ in range(t):
    n = int(input())

    p = list(map(int, input().split()))
    
    p = [0] + p + [0]  
    
    ans = []
    for i in range(1, n + 1):
        if (i == 1 or i == n or (p[i-1] < p[i]) != (p[i] < p[i+1])):
            ans.append(p[i])
                     
    print(len(ans))
    print(' '.join(map(str, ans)))
