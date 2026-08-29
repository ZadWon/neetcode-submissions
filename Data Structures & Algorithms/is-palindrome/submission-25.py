class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0,len(s)-1
        while i < j:
            if self.check_alpha_num(s[i]):
                i += 1
                continue
            if self.check_alpha_num(s[j]):
                j = j-1
                continue
            if s[i].lower() != s[j].lower():
                # print(f"i = {i}, j = {j}")
                # print(f"s[i] = {s[i]}, s[j] = {s[j]}")
                return False
            i += 1
            j -= 1
        return True

    def check_alpha_num(self, c):
        if (ord("a") <= ord(c) <= ord("z")) or (ord("A") <= ord(c) <= ord("Z")) or ord("0") <= ord(c) <= ord("9"):
            
            return False
        return True