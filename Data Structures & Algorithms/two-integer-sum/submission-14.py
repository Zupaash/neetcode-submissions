class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = []

        for i in range(len(nums)):
            pairs.append((nums[i], i))
        
        pairs.sort(key=lambda x:x[0])

        left = 0

        right = len(nums) - 1

        while left < right:
            le_sum = pairs[left][0] + pairs[right][0]

            if le_sum == target:
                return sorted([pairs[left][1], pairs[right][1]])
            elif le_sum < target:
                left = left + 1
            elif le_sum > target:
                right = right - 1

        return [] 