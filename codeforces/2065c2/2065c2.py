import bisect
 
def solve():
    import sys
    input = sys.stdin.readline
    
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        b.sort()
        
        prev = -10**18
        ok = True
        
        for x in a:
            best = 10**18
            
            if x >= prev:
                best = x
            
            target = prev + x
            j = bisect.bisect_left(b, target)
            if j < m:
                val = b[j] - x
                if val >= prev:
                    best = min(best, val)
            
            if best == 10**18:
                ok = False
                break
            
            prev = best
        
        print("YES" if ok else "NO")
solve()