"""
Implement a function compress_string that performs basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string, your method should return the original string.
"""
from typing import List


def string_compression(s: str) -> str:
    #Handling empty string
    if not s:
        return s

    final_string = ""
    counter = 0
    for i in range(len(s)):
        counter += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            final_string = final_string + s[i] + str(counter)
            counter = 0
    return final_string if len(final_string) < len(s) else s

# Return a boolean value if the given string is palindrome. Only consider alphanumeric characters.
def valid_palindrome(s: str) -> bool:
    cleaned_string = ("".join(char for char in s if char.isalnum())).lower()
    reverse_string = cleaned_string[::-1]
    return True if reverse_string == cleaned_string else False

# Defang an IP address(make '.' '[.]')
def defang_ip(s: str) -> str:
    list = []
    for char in s:
        if char == '.':
            list.append('[.]')
        else:
            list.append(char)
    return "".join(list)

# String compression list
def string_compress_list(list : List[str]) -> int:
    count = 0
    result = []
    for i in range(len(list)):
        count += 1
        if i + 1 >= len(list) or list[i] != list[i+1]:
            result.append(list[i])
            result.append(count)
            count = 0
    return result

# Valid palindrome 2: Return true if the string is palindrome or if not, then it could be if atmost 1 character can be deleted
def valid_palindrome_two(strs: str) -> bool:
    left = 0
    right = len(strs) - 1
    while left < right:
        if strs[left] != strs[right]:
            str_left = strs[left:right]
            rev_str_left = str_left[::-1]
            str_right = strs[left+1:right+1]
            rev_str_right = str_right[left+1:right+1]
            if str_left == rev_str_left or str_right == rev_str_right:
                return True
            else:
                return False
        left += 1
        right -= 1
    return True

#reverse words in a string and return
def reverse_words(strs: str) -> str:
    split_string = strs.split()
    return " ".join(split_string[::-1])

#Longest substring without repeating characters
def longest_substring_without_repeating_characters(strs: str) -> int:
    longest = 0
    left = 0
    seen = {}
    for right in range(len(strs)):
        char = strs[right]
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        count = right - left + 1
        longest = max(longest, count)
    return longest

#Find all the palindromic substrings in the given string
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

strs = "abc"
print(count_substring(strs))