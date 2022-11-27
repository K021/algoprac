# https://leetcode.com/problems/sum-of-subarray-minimums/description/

from typing import List

from modules import TestManager, TestCase

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        sumi = 0
        for i, v in enumerate(arr):
            l, r = i - 1, i + 1
            lcount = rcount = 0 
            while 0 <= l and arr[l] > v:
                lcount += 1
                l -= 1
            while r < n and arr[r] >= v:
                rcount += 1
                r += 1
            count = 1 + lcount + rcount + lcount * rcount
            print(f"{i=}, {v=}, {count=}")
            sumi += v * count
        return sumi % (10**9 + 7)

test_cases = [
    TestCase(input=([3, 1, 2, 4],), output=17),
    TestCase(input=([11, 81, 94, 43, 3],), output=444),
    TestCase(input=([71, 55, 82, 55],), output=593),
]

if __name__ == "__main__":
    test_manager = TestManager(test_cases=test_cases)
    test_manager.run(Solution().sumSubarrayMins)
