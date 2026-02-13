class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        pairing= {}
        paired = set()
        

        for ch, word in zip(pattern,words):
            if ch in pairing:
                if pairing[ch] != word:
                    return False
            else:
                if word in paired:
                    return False
                pairing[ch] = word
                paired.add(word)
        return True

        

         
        