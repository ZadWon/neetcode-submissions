class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)
        while l<r:
            if r == l+1 and nums[r-1] != target and nums[l] != target:
                return -1
            if nums[l+(r-l) // 2] == target:
                return l+ (r-l)//2
            elif nums[l+(r-l)//2] > target:
                r = l+(r-l)//2
                print(r)


            else:
                l = l + (r-l)//2
                print(l)


        return -1
