class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        skill_sum = skill[0] + skill[len(skill)-1]
        left = 1
        right = len(skill)-2

        chem = 0
        chem+= skill[0] * skill[len(skill)-1]
        found = True
        count = 1

        while left < right:
            chem_sum = skill[left] + skill[right]

            if chem_sum == skill_sum:
                chem+= (skill[left] * skill[right])
                count+= 1
            else:
                found = False
                
            left+=1
            right-=1
    
        if found and (count == (len(skill)/2)):
            return chem
        else:
            return -1
