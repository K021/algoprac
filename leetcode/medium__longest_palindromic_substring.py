# https://leetcode.com/problems/longest-palindromic-substring/description/

from modules import TestManager, TestCase


# Time Limit Exceeded
class Solution1:
    @staticmethod
    def palindromic(s: str):
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True
    def longestPalindrome(self, s: str) -> str:
        if self.palindromic(s):
            return s
        right_max = self.longestPalindrome(s[1:])
        left_max = self.longestPalindrome(s[:-1])
        return right_max if len(right_max) > len(left_max) else left_max


# Time Limit Exceeded
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        middle_max = ""
        if s[0] == s[-1]:
            ms = s[1:-1]
            middle_max = self.longestPalindrome(ms)
            middle_max = s if len(middle_max) == len(ms) else middle_max
        right_max = self.longestPalindrome(s[1:])
        left_max = self.longestPalindrome(s[:-1])

        return max(middle_max, right_max, left_max, key=len)


test_cases = [
    TestCase(input=("babad",), output=["bab", "aba"], operator="__contains__"),
    TestCase(input=("cbbd",), output="bb"),
    TestCase(input=("a",), output="a"),
]


if __name__ == '__main__':
    test_manager = TestManager(test_cases=test_cases)
    test_manager.run(Solution().longestPalindrome)