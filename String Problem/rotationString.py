# https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/
# Check if given strings are rotations of each other or not

'''
    Input: S1 = ABCD, S2 = CDAB
    Output: Strings are rotations of each other

    Input: S1 = ABCD, S2 = ACBD
    Output: Strings are not rotations of each other
'''


s1 = 'abcde'
s2 = 'cdeab'
def checkRotate():
    if len(s1) == len(s2):
        s3 = s1 + s1
        if s2 in s3:
            return True
    return False

s = checkRotate()
print(s)
    