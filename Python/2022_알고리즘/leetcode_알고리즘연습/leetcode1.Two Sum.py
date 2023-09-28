from collections import defaultdict
class Solution:
    def twoSum(self, nums: list, target: int):
        dic = defaultdict(int)

        for i in range (len(nums)):
            cur = nums[i]
            needValue = target - nums[i]
            if (needValue in dic):
                return [dic[needValue],i]
            else:
                dic[cur] = i

        return []

# Runtime: 60 ms, faster than 97.12% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 54.36% of Python3 online submissions for Two Sum.
# print(Solution.twoSum(Solution, [3,2,4], 6))
# print(Solution.twoSum(Solution, [3,3], 6))
