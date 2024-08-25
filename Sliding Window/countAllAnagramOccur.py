class Solution:

    def allZero(self, freq):
        for i in freq:
            if (i != 0):
                return False
        return True 

    def countAllOccur(self, txt, pat):

        txt_len = len(txt)
        pat_len = len(pat)
        freq = [0] * 26
        for i in pat:
            val = ord(i) - ord('a')
            freq[val] += 1 
        i = j = 0
        result = 0
        while j < txt_len:
            freq[ord(txt[j]) - ord('a') ] -= 1 
            if (j - i + 1 == pat_len):
                if(self.allZero(freq)):
                    result += 1
                freq[ord(txt[i]) - ord('a')]  += 1 
                i+= 1
            j += 1
        return result
    
ob = Solution()
txt = 'abab'
pat = 'ab'
res = ob.countAllOccur(txt, pat)
print(res)

