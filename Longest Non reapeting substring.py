#Leetcode qustion Link:  https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookUp=set()
        l,r=0,0
        maxLen=0
        while r<len(s):
            if s[r] not in lookUp:
                lookUp.add(s[r])
                maxLen=max(maxLen,len(lookUp))
                r+=1
            else:
                lookUp.remove(s[l])
                l+=1
        return maxLen
