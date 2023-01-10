# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false

# Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [i for i in s]
        t_list = [x for x in t]
        if len(s_list) != len(t_list):
            return False
        return sorted(s_list) == sorted(t_list)