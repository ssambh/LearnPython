from typing import List


class ArrayPractice:
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

    # Find 2 numbers from the list which add upto the target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in dic:
                return [dic[diff], i]
            dic[nums[i]] = i