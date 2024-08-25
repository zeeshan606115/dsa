# https://leetcode.com/problems/valid-anagram

class Soultion:
    def isAnagram(self, s, t):
        freq = [0] * 26
        for i in s:
            freq[ord(i) - ord('a')] += 1 
        for i in t:
            freq[ord(i) - ord('a')] -= 1

        for i in freq:
            if i != 0:
                return False
        return True

obj = Soultion()
s = "anagram"
t = "nagaramd"
res = obj.isAnagram(s, t)  
print(res)