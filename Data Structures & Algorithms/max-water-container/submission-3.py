class Solution:
    def maxArea(self, heights: List[int]) -> int:
        tmp = 0
        current = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                a = min(heights[i], heights[j])
                # print(a)
                b= j-i
                
                tmp = a * b
                if tmp > current:
                    current = tmp
        return current