from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ran=Counter(ransomNote)
        count_mag=Counter(magazine)
        for  letter in count_ran:
            if count_ran[letter]>count_mag.get(letter,0):
                return False
        return True