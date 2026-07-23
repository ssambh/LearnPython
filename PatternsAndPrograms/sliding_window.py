from typing import List


class Slidingwindow:
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

    #Find the longest palindromic substring
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