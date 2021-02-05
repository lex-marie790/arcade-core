"""
Given an integer n, return the largest number that contains exactly n digits.

Example

For n = 2, the output should be
largestNumber(n) = 99.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 9.

[output] integer

The largest integer of length n.
"""

"""
For each number, the n represents a number(length) and we need to print out 9x the length
1 = 9
2 = 99
3 = 999
4 = 9999

"""
def largestNumber(n):
    num = 0
    for i in range(0, n):
        num += 9*pow(10,i)
    return num
        
        