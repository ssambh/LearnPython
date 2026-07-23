# Group anagrams - Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict

# Group the anagrams from the given list of anagrams together
class dic:
    def group_anagrams(self, strs):
        dict = defaultdict(list)
        for word in strs:
            dict["".join(sorted(word))].append(word)
        return list(dict.values())

#Longest substring without repeating characters
    def longest_substr_without_repeating_char(self, strs):
        count_dict = {}
        left = 0
        count = 0
        max_len = 0
        for right in range(len(strs)):
            char = strs[right]
            if char in count_dict and count_dict[char] >= left:
                left = count_dict[char] + 1
            count_dict[char] = right
            count = right - left + 1
            max_len = max(max_len,count)

        return max_len


obj = dic()
strs = "pwwkew"
print(obj.longest_substr_without_repeating_char(strs))
