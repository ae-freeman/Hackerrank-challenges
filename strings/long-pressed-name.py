# Your friend is typing his name into a keyboard.  Sometimes, when typing a character c,
# the key might get long pressed, and the character will be typed 1 or more times.
#
# You examine the typed characters of the keyboard.  Return True if it is possible
# that it was your friends name, with some characters (possibly none) being long pressed.
#
#
#
# Example 1:
#
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# Example 2:
#
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
# Example 3:
#
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# Example 4:
#
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
#
#
# Note:
#
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.
#

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        a,b = 0,0
        stack = []
        while a <len(name) and b<len(typed):
            if name[a] == typed[b]:
                stack.append(typed[b])
                a += 1
                b += 1
            else:
                if stack == []:
                    return False
                else:
                    if typed[b] == stack[-1]:
                        b += 1
                    else:
                        a +=1
                        b +=1
        print(stack)
        print(''.join(stack))
        return ''.join(stack) == name
