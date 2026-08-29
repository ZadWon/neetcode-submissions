class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers_openers = {"]" : "[", ")" : "(", "}" : "{"}

        for c in s:
            if (c in closers_openers and len(stack)):
                if (stack[-1] == closers_openers[c]):
                    stack.pop()
                else :
                    return (False)
            else:
                stack.append(c)
        if (len(stack) == 0):
            return True 
        else:
            return False