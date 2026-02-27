n, s = map(int, input().split())

segments = list(map(int,input().split()))

good = 0
left = 0

count = 0

for right in range(len(segments)):
    good += segments[right]

    while good > s:
        good -= segments[left]
        left += 1
    
    count += right - left + 1
   
print(count)
