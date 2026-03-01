t = int(input())

for _ in range(t):

    n = int(input())
    a = input().strip()
    b = input().strip()

    a += '0'
    b += '0'
    cnt = 0
    check = True

    for i in range(n):
        if a[i] == '1':
            cnt += 1
        else:
            cnt -= 1
        if ((a[i] == b[i]) != (a[i + 1] == b[i + 1])) and cnt != 0:
            print("NO")
            check = False
            break
    if check: 
        print("YES")

