class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap=dict()
        seen=set()
        for index,character  in enumerate(s) :
            if character  in seen :
                if character in hashmap:
                    del hashmap[character]
            else :
                hashmap[character]=index
                seen.add(character)
        
           
        if  hashmap==dict():
            return -1
        else :
            return min(hashmap.values())