test = int(input())

from collections import Counter

for _ in range(test):
    s = input()
    t = input()
    
    count_t = Counter(t)
    count_s = Counter(s)
    
    possible = True
    
    for ch in count_s:
        if count_s[ch] > count_t[ch]:
            print("Impossible")
            possible = False
            break
        count_t[ch] -= count_s[ch]
    
    if not possible:
        continue
    
    t_prime = []
    for ch in count_t:
        t_prime.extend([ch] * count_t[ch])
    
    t_prime.sort()
    
    i = 0
    j = 0
    result = []

    while i < len(s) and j < len(t_prime):
        if s[i] <= t_prime[j]:
            result.append(s[i])
            i += 1
        else:
            result.append(t_prime[j])
            j += 1

    result.extend(s[i:])
    result.extend(t_prime[j:])
    
    print(''.join(result))
