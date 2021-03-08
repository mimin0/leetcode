class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        goal = []
        for i in nums:
            indexA = nums.index(i)
            remain = target - i
            if remain in nums:
                indexB = nums.index(remain)
                return [indexA, indexB]
