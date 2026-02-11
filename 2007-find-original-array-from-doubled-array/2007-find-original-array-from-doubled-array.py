class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count=Counter(changed)
        ans=[]
        if len(changed)%2!=0:
            return []
        for num in changed:

            if not count[num]:
                continue
            if not count[num*2]:
                return []

            count[num]-=1
            count[num*2]-=1
            ans.append(num)

        return (ans)
