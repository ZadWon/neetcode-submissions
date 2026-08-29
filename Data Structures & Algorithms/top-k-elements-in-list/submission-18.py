class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        bucket = [[] for i in range(len(nums) + 1)]
        print(bucket)
        for h,v in count.items():
            bucket[v].append(h)
        res = []
        for i in range(len(nums), 0, -1):
            for h in range(len(bucket[i])):
                res.append(bucket[i][h])
                if len(res) == k :
                    print(res)
                    return res
