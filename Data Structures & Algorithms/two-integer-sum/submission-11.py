class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # for i in range(len(nums)) :
        #     hashmap[nums[i]] = i
        
        for i in range(len(nums)) :
            
            if hashmap.get(target - nums[i], 'x') != 'x' :

                return [hashmap[target - nums[i]], i] 

            hashmap[nums[i]] = i