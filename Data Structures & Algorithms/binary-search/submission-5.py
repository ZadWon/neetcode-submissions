class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        r = len(nums) - 1
        l = 0

        while (l <= r):
            div = l + (r - l) 
            if ( nums[div] > target):
                r = div - 1
            elif (nums[div] < target):
                l = div + 1
            else:
                return (div)
        return -1
