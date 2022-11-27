# https://leetcode.com/problems/sum-of-subarray-minimums/description/

from typing import List

from modules import TestManager, TestCase


# Time Limit Exceeded
class Solution1:
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


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = [0] * len(arr)
        for i, a in enumerate(arr):
            while stack and stack[-1][0] > a:
                stack.pop()
            if stack:
                res[i] = (i - stack[-1][1]) * a + res[stack[-1][1]]
            else:
                res[i] = (i + 1) * a
            stack.append((a, i))
        return sum(res) % (10 ** 9 + 7)


class SolutionOther1:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # monotonic increasing stack
        stack = []

        # make a dp array of the same size as the input array
        dp = [0] * len(arr)

        # populate monotonically increasing stack
        for i in range(len(arr)):
            # before pushing an element, make sure all
            # larger and equal elements in the stack are
            # removed
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            # calculate the sum of minimums of all subarrays
            # ending at index i
            if stack:
                previousSmaller = stack[-1]
                dp[i] = dp[previousSmaller] + (i - previousSmaller) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]
            stack.append(i)

        # add all the elements of dp to get the answer
        return sum(dp) % MOD


class SolutionOther2:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #Time: O(n)
        #Space: O(n)
        modifiedArr = [0] + arr
        result = [0]*len(modifiedArr)
        stack = [0]
        for i in range(len(modifiedArr)):
            while modifiedArr[stack[-1]] > modifiedArr[i]:
                stack.pop() 
            previousIndex = stack[-1] #Guaranteed to be 0 if we end up emptying the stack as we have 0 always there
            result[i] = result[previousIndex] + (i- previousIndex)*modifiedArr[i]
            stack.append(i)
        return sum(result) % (10**9+7)


test_cases = [
    TestCase(input=([3, 1, 2, 4],), output=17),
    TestCase(input=([11, 81, 94, 43, 3],), output=444),
    TestCase(input=([71, 55, 82, 55],), output=593),
]

if __name__ == "__main__":
    test_manager = TestManager(test_cases=test_cases)
    test_manager.run(Solution().sumSubarrayMins)
