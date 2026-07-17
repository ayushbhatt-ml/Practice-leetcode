class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target - nums[i] in nums:
                temp = nums.index(target-nums[i])
                result = [i,temp]
                if i == temp:
                    continue
                return result
        