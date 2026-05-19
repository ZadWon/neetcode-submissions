class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     k = ''.join(sorted(s))
    #     l = ''.join(sorted(t))
        
    #     for i in range(len(s)):
    #         if k[i] != l[i]:
    #             return False
    #     return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterS, counterT = {}, {}

        for i in range(len(s)):
            counterS[s[i]] = 1+ counterS.get(s[i], 0)
            counterT[t[i]] = 1+ counterT.get(t[i], 0)
        return counterS == counterT




