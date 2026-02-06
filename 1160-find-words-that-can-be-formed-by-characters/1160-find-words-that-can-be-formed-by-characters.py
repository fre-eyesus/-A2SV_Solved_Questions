class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        char_count = {}
        for c in chars:
            char_count[c] = char_count.get(c, 0) + 1
        
        total_length = 0
        
        for word in words:
         
            word_count = {}
            for c in word:
                word_count[c] = word_count.get(c, 0) + 1
            
           
            valid = True
            for c, count in word_count.items():
                if c not in char_count or char_count[c] < count:
                    valid = False
                    break
            
            if valid:
                total_length += len(word)
        
        return total_length