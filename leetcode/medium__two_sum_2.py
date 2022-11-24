# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

from modules import TestManager, TestCase

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l+1, r+1]
            if s > target:
                r -= 1
            else:
                l += 1
        raise Exception("No Answer")


test_cases = [
    TestCase(input=([2, 7, 11, 15], 9), output=[1, 2]),
    TestCase(input=([2, 3, 4], 6), output=[1, 3]),
    TestCase(input=([-1, 0], -1), output=[1, 2]),
]

if __name__ == "__main__":
    test_manager = TestManager(test_cases=test_cases)
    test_manager.run(Solution().twoSum)
