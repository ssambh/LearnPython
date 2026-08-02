from collections import Counter
from typing import List


class QAPracticePrograms:
    #Reverse a string
    def reverse_string(self, strs: str) -> str:
        return strs[::-1]

    #Find if the given string is palindrome, ignoring all the non-alphanumeric characters
    def verify_palindrome(self, strs: str) -> bool:
        clean_string = "".join(char.lower() for char in strs if char.isalnum())
        if clean_string == clean_string[::-1]:
            return True
        else:
            return False

    #Return the index of the first character in the string that appears once
    def return_first_non_repeating_char(self, strs: str) -> int:
        count = Counter(strs)
        for index, char in enumerate(strs):
            if count[char] == 1:
                return index
        return None

    #Find if 2 strings are anarams
    def anagrams(strs: str, strst: str):
        s = strs
        t = strst

        maps = {}
        mapt = {}

        if len(s) != len(t):
            return False
        for i in s:
            maps[i] = maps.get(i, 0) + 1
        for i in t:
            mapt[i] = mapt.get(i, 0) + 1
        if maps != mapt:
            return False
        else:
            return True
    # Find the longest common prefix form the list of strings given
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(prefix)):
            for string in strs:
                if i == len(string) or string[i] != prefix[i]:
                    return prefix[:i]
        return prefix

    # Determine if the two given strings are isomorphic
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dics = {}
        dict = {}
        for i in range(len(s)):
            if s[i] in dics.keys():
                if dics[s[i]] != t[i]:
                    return False
            if t[i] in dict.keys():
                if dict[t[i]] != s[i]:
                    return False
            dict[t[i]] = s[i]
            dics[s[i]] = t[i]
        return True

    # Find 2 numbers from the list which add upto the target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in dic:
                return [dic[diff], i]
            dic[nums[i]] = i

    # Move all the zeroes to the right of the list
    def moveZeroes(self, nums: List[int]) -> None:
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
            right += 1

    # Maximum Subarray (Kadane’s Algorithm): Find the contiguous subarray which has the largest sum.
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maximum = float('-inf')
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            total += i
            maximum = max(maximum, total)
            if total < 0:
                total = 0
        return maximum

    # Merge Sorted Arrays: Merge two sorted arrays into one large sorted array without using extra space.
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        curr = len(nums1) - 1
        while i >= 0 and j >= 0:

            if nums2[j] > nums1[i]:
                nums1[curr] = nums2[j]
                j -= 1
            else:
                nums1[curr] = nums1[i]
                i -= 1
            curr -= 1

        if i < 0:
            while j >= 0:
                nums1[curr] = nums2[j]
                j -= 1
                curr -= 1
        if j < 0:
            while i >= 0:
                nums1[curr] = nums1[i]
                i -= 1
                curr -= 1
    # Remove Duplicates from Sorted Array: Remove duplicates in-place such that each unique element appears only once.
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1
        while r < len(nums):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l

    # Best Time to Buy and Sell Stock: Find the maximum profit you can achieve from buying and selling a stock on different days. - Leetcode 121
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = sell = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy = sell
            max_profit = max(profit, max_profit)
            sell += 1
        return max_profit

    #Rotate Array: Rotate an array to the right by k steps. - Leetcode 189
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # 1. Handle cases where k is larger than the array length
        k = k % n

        # If k becomes 0 after modulo, no rotations are needed
        if k == 0:
            return
        nums = self.swap_func(nums, 0, len(nums) - 1)

        nums = self.swap_func(nums, 0, k - 1)
        print(nums)
        nums = self.swap_func(nums, k, len(nums) - 1)
        print(nums)

    def swap_func(self, nums: List[int], start, end) -> List[int]:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums

    # Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times. - Leetcode 229
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = int(len(nums) / 3)
        result = []
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1
        for i, j in map.items():
            if j > n:
                result.append(i)
        return result

obj = QAPracticePrograms()
print(obj.maxProfit([7,6,4,3,1]))