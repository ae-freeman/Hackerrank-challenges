# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: "III"
# Output: 3
# Example 2:
#
# Input: "IV"
# Output: 4
# Example 3:
#
# Input: "IX"
# Output: 9
# Example 4:
#
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution:
    def romanToInt(self, s: str) -> int:

        int_to_join = []

        #if char is I, x, or C: check what the next value is.

        i = 0

        while i < len(s):
            if s[i] == 'I' or s[i] == 'X' or s[i] == 'C':
                if i < len(s) - 1:
                    if s[i] == 'I' and s[i+1] == 'V':
                        number = 4
                        int_to_join.append(number)
                        i += 2
                        continue
                    elif s[i] == 'I' and s[i+1] == 'X':
                        number = 9
                        int_to_join.append(number)
                        i += 2
                        continue
                    elif s[i] == 'X' and s[i+1] == 'L':
                        number = 40
                        int_to_join.append(number)
                        i += 2
                        continue
                    elif s[i] == 'X' and s[i+1] == 'C':
                        number = 90
                        int_to_join.append(number)
                        i += 2
                        continue
                    elif s[i] == 'C' and s[i+1] == 'D':
                        number = 400
                        int_to_join.append(number)
                        i += 2
                        continue
                    elif s[i] == 'C' and s[i+1] == 'M':
                        number = 900
                        int_to_join.append(number)
                        i += 2
                        continue



            if s[i] == 'I':
                number = 1
                int_to_join.append(number)
                i +=1
            elif s[i] == 'V':
                number = 5
                int_to_join.append(number)
                i +=1
            elif s[i] == 'X':
                number = 10
                int_to_join.append(number)
                i +=1
            elif s[i] == 'L':
                number = 50
                int_to_join.append(number)
                i +=1
            elif s[i] == 'C':
                number = 100
                int_to_join.append(number)
                i +=1
            elif s[i] == 'D':
                number = 500
                int_to_join.append(number)
                i +=1
            elif s[i] == 'M':
                number = 1000
                int_to_join.append(number)
                i +=1
        

        result = sum(int_to_join)
        return result
