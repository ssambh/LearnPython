from collections import deque
from typing import List


class Blind75:
    # Longest consecutive sequence without repeating character - Leetcode 128
    def longest_consecutive_sequence(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for i in sett:
            current = i
            if current - 1 not in sett:
                count = 1
                while current + 1 in sett:
                    count += 1
                    current += 1
                longest = max(longest, count)
        return longest

    # Find all the palindromic substrings in the given string - Leetcode 647
    def count_substring(s: str) -> int:
        count = 0
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                else:
                    break
                left -= 1
                right += 1
            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                else:
                    break
                left -= 1
                right += 1
        return count

    #Find the longest palindromic substring - Leetcode 5
    def longestPalindrome(self, s: str) -> str:
        count = 0
        longest = ""
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    sub = s[left:right + 1]
                    if len(longest) < len(sub):
                        longest = sub
                else:
                    break
                left -= 1
                right += 1

            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    sub = s[left:right + 1]
                    if len(sub) > len(longest):
                        longest = sub
                else:
                    break
                left -= 1
                right += 1
        return longest

    # Find the missing number in the list of numbers in range [0,n] - Leetcode 268
    def missing_number(self,nums: List[int]) -> int:
        total = 0
        for i in nums:
            total += i
        length = len(nums)
        missing = (length * (length + 1)) / 2 - total
        return int(missing)

    #Valid parentheses - Leetcode 20
    def isValid(self, s: str) -> bool:
        stack = deque()
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        for i in s:

            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif not stack:
                return False
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(prefix)):
            for string in strs:
                if i == len(string) or string[i] != prefix[i]:
                    return prefix[:i]
        return prefix
