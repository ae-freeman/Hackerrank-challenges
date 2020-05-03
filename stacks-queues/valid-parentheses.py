# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:

        # initialise a stack (list)

        stack = []
        last_item = len(stack) - 1

        # for each char in string
        for i in range(len(s)):


            # check if opening ({[, or closing )}]
            if s[i] == '(' or s[i] == "{" or s[i] == '[':

                # if opening, add it to the stack
                stack.append(s[i])

            # if closing, see if equals the bracket on the top of the stack.
            else:
                if len(stack) == 0:
                    return False
                # if it does, then pop/remove the top item on the stack
                if stack[last_item] == "(" and s[i] == ")":
                    stack.pop()
                elif stack[last_item] == "{" and s[i] == "}":
                    stack.pop()
                elif stack[last_item] == "[" and s[i] == "]":
                    stack.pop()

                # else return false
                else:
                    return False


        if len(stack) == 0:
            return True
        else:
            return False
