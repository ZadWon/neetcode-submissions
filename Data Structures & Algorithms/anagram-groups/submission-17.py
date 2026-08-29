class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        result= []
        for i in range(len(strs)):
            # strs[i].sorted()
            hashmap.setdefault(tuple(sorted(strs[i])), []).append(strs[i])
        for key in hashmap:
            result.append(hashmap[key])
        print(result)
        return result
