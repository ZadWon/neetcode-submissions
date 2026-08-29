class Solution:

    def encode(self, strs: List[str]) -> str:
        cipher = ""
        for s in strs:
            cipher = cipher + str( len(s)) + "#" + s
        print(cipher)
        return cipher
    def decode(self, s: str) -> List[str]:
        b = 0
        a=0
        index= 0
        res= []
        for i in range(len(s)): 
            if s[i] == '#' and i >= b :
                
                count = s[b:i]
                print(f'i = {i} count= {count} a= {a} b= {b}')
                a = i+1
                b = a + int(count)
                res.append( s[i+1 : b] )
                
        print(res)
        return res