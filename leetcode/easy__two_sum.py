# https://leetcode.com/problems/two-sum/submissions/

from typing import List

from modules import TestManager
from modules import TestCase

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        nums = [(val, idx) for idx, val in enumerate(nums)]
        nums = sorted(nums)
        while l < r:
            s = nums[l][0] + nums[r][0]
            if s == target:
                return [nums[l][1], nums[r][1]]
            if s > target:
                r -= 1
            else:
                l += 1
        raise Exception("No Answer")

INPUTS_AND_OUTPUTS = [
    TestCase(input=([2, 7, 11, 15], 9), output=[0, 1]),
    TestCase(input=([3, 2, 4], 6), output=[1, 2]),
]

if __name__ == "__main__":
    test_manager = TestManager(INPUTS_AND_OUTPUTS)
    test_manager.run(Solution().twoSum)
