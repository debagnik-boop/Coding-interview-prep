#Leetcode Link: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def process(self,s):
        s=s.replace(" ","")
        for ele in s:
            if not ele.isalnum():
                s=s.replace(ele,"")
        s=s.lower()
        return s
    
    def isPalindrome(self, s: str) -> bool:
        s=self.process(s)
        l,r=0,len(s)-1
        while(l<=r):
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
