class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums= sorted(nums)
        tmp= 1
        res=1
        if len(sortedNums) == 0:
            return 0
        for i in range(len(sortedNums)-1):
            if sortedNums[i] == sortedNums[i+1]:
                continue
            if sortedNums[i+1] == sortedNums[i] + 1:
                tmp +=1
                if tmp > res:
                    res = tmp
            else:
                tmp = 1
        return res