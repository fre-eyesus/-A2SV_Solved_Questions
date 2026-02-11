t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = 10**9

    for i in range(n):

  
        if i+1 < n and s[i:i+2] == "aa":
            ans = min(ans,2)

   
        if i+2 < n:
            if s[i:i+3] in ("aba","aca"):
                ans = min(ans,3)

        if i+3 < n:
            if s[i:i+4] in ("abca","acba"):
                ans = min(ans,4)


        if i+6 < n:
            if s[i:i+7] in ("abbacca","accabba"):
                ans = min(ans,7)

    print(ans if ans!=10**9 else -1)
