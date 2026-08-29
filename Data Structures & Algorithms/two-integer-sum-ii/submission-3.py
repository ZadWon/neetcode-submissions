# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         right = len(numbers) - 1
#         left = 0
#         while left < right:
#             if numbers[left] + numbers[right] == target:
#                 return [left+1, right+1]
#             elif numbers[left] + numbers[right] > target :
#                 if numbers[left] > numbers[right]:
#                     left += 1
#                 else:
#                     right -=1
#             else:
#                 if numbers[left] < numbers[right]:
#                     left += 1
#                 else:
#                     right -=1
                 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []