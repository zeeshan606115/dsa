# https://www.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1

'''
    Input: str = "aaaabbaa"
    Output: "aabbaa"
'''

st = 'aaaabbaa'
max_pal = 1
val = st[0]
left = 0
right = len(st) - 1
for i in range(len(st)):
    if st[left] == st[right]:
        pass