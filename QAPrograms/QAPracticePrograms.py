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

obj = QAPracticePrograms()
print(obj.isIsomorphic("egg", 'add'))