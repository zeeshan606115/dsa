class Solution:

    def allZero(self, freq):
        for i in freq:
            if (i != 0):
                return False
        return True 

    def findAnagrams(self, txt, pat):

        txt_len = len(txt)
        pat_len = len(pat)
        freq = [0] * 26
        for i in pat:
            val = ord(i) - ord('a')
            freq[val] += 1 
        i = j = 0
        lst = []
        while j < txt_len:
            freq[ord(txt[j]) - ord('a') ] -= 1 
            if (j - i + 1 == pat_len):
                if(self.allZero(freq)):
                    lst.append(i)
                freq[ord(txt[i]) - ord('a')]  += 1 
                i+= 1
            j += 1
        return lst
    
ob = Solution()
txt = 'abab'
pat = 'ab'
res = ob.findAnagrams(txt, pat)
print(res)

