"""
Problem Statement : Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return 

        # Find the shortest string in the list
        min_len = min(len(s) for s in strs)
        
        # Initialize the result string
        result = ""

        # Iterate through each character position
        for i in range(min_len):
            # Get the character at position i in the first string
            char = strs[0][i]
            
            # Check if this character is common among all strings
            if all(s[i] == char for s in strs):
                result += char
            else:
                break
        
        return result
