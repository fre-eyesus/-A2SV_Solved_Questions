class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
     
        n = len(list1)
        m = len(list2)
        ans = {}
        for i in range(n):
            for j in range(m):
                if list1[i] == list2[j]:
                    ans[list1[i]] = [i + j]
        min_sum = min(ans.values())
        result = []

        for key, value in ans.items():
            if value == min_sum:
                result.append(key)

        return result     
                
                        
        
        return ans

                    
                    