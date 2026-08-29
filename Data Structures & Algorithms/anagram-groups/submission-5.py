class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for s in strs:
            # 1. Sort the string and convert to a tuple (which IS hashable!)
            key = tuple(sorted(s))
            
            # 2. Add the string to the hashmap safely
            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(s)
            
        # 3. The hashmap's values are already the grouped lists!
        return list(hashmap.values())