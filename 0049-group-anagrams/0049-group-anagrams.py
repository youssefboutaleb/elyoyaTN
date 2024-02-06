class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=dict()
        for string in strs :
            key=''.join(sorted(string))
            if key in map:
                map[key].append(string)
            else :
                map[key]=[string]
        return list(map.values())
            