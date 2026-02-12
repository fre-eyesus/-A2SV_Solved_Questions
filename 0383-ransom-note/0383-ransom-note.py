class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        count = 0
        for char in ransomNote:
            if ransom_count[char] == magazine_count[char]:
                count+=1
        return count == len(ransomNote)
        