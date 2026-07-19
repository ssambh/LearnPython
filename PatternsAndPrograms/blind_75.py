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