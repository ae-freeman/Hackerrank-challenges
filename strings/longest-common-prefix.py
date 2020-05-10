# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # For every letter in the first word
        # Save first letter.
        # For each word, check it matches that letter
        # If this, occurs, save the first two letters of first word to variable
        # Check again

        prefix = ""
        stop_loop = False

        if len(strs) != 0:
            for i in range(len(strs[0]) + 1):
                prefix = strs[0][0:i]
                for j in range(1, len(strs)):
                    if strs[j][0:i] != prefix:
                        stop_loop = True
                        break

                if stop_loop == True:
                    prefix = prefix[:-1]
                    break

        return prefix
