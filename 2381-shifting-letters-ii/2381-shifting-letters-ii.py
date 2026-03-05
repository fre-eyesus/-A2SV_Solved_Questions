class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * (len(s) )

        for l, r, d in shifts:
            if d == 0: 
                for i in range(l,r+1):
                    prefix_sum[i] -= 1

            else: 
                for j in range(l,r+1):
                    prefix_sum[j] += 1
            

        accumulate = 0
        answer = ''
        for i, char in enumerate(s):
            char_ord = ord(char) - ord('a') 
            
            accumulate = prefix_sum[i]

            new_ord = (char_ord + accumulate) % 26
            answer += chr(new_ord + ord('a'))

        return answer