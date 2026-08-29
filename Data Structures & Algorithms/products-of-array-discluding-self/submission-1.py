class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp= 1
        tmp_0 = 1
        zeros = 0
        res = []
        for num in nums: 
            if num != 0:
                tmp = tmp * num
            else:
                
                zeros = zeros + 1
        print(f"zeros : {zeros} , tmp : {tmp}")

        if zeros > 1:
            tmp = 0

        for num in nums: 
            
            if num == 0 and zeros >= 1:
                res.append(tmp)
            elif zeros == 1:
                res.append(0)
            else:
                res.append(tmp//num)
        return res