class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums)):
            diff = target - nums[i]

            if(diff in nums[0:i]):
                return [i, nums[0:i].index(diff)]
            elif(diff in nums[i + 1:]):
                return [i, nums[i + 1:].index(diff) + (i + 1)]