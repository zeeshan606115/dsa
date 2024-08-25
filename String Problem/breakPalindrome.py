# https://leetcode.com/problems/break-a-palindrome/description/
'''
Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

'''

'''
Solution:- 
first we are checking if length < 2 then returning ""

if not then Replace First Non-'a' Character: Iterate through the string. For the first character that is not 'a', 
replace it with 'a'. If this transformation makes the string non-palindromic, return it immediately.

After replacing the first non-'a' character, 
check if the resulting string is a palindrome. If it is, continue to the next character.
then at the end replace the last character with 'b'
'''

palindrome = "abccba"
def breakPalindrome(palindrome) :
    st = list(palindrome)
    if (len(st) < 2):
        return ""
    
    for i in range(len(st) // 2):
        if st[i] !='a':
            st[i] ='a'
            return ''.join(st)
    st[-1] = 'b'
    return ''.join(st)

result = breakPalindrome(palindrome)
print(result)