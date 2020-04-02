# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x: int) -> int:

        #### Can also do this by truncating the end of the int and adding to a list, see below

        string_int = str(x)
        reversed = string_int[::-1]

        if reversed == '0':
            return 0
        else:

            count_zeros = 0

            for char in reversed:
                if char == '0':
                    count_zeros += 1
                else:
                    break

            number = reversed[count_zeros:]
            print(number)

            number_len = len(number)

            if number[number_len - 1] == '-':
                final = int('-' + number[:number_len-1])
            else:

                final = int(number)




            if final > 2147483646 or final < -2147483647:
                return 0
            else:
                return final



        # OTHER method
        class Solution:
            # @param {integer} x
            # @return {integer}
            def reverse(self, x):
                arr = []
                f = False
                if x < 0:
                    x *= -1
                    f = True
                while True:
                    arr.append(x % 10)
                    x /= 10
                    if x == 0:
                        break
                result = 0
                for i in arr:
                    result = i + 10 * result
                if f:
                    result *= -1
                return result
