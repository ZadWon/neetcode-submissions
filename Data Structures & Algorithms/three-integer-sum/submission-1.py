class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res=[]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 sortedRes = [nums[i], nums[j], nums[k]]
        #                 sortedRes.sort()
        #                 if sortedRes not in res:
        #                     res.append(sortedRes)
        # return res
        s= {}
        res = []
        for i in range(len(nums)):
            s[nums[i]] = i
        print(s)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = - nums[i] - nums[j]
                if (diff in s) and (s[diff] not in [i,j] ):
                    tmp = [nums[i] , nums[j], diff ]
                    print(tmp)
                    if sorted(tmp) not in res:
                        res.append(sorted(tmp))

        return res


