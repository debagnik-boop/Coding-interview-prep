// Leetcode link: https://leetcode.com/problems/valid-palindrome-ii/

class Solution {
public:
    bool validSub(string s,int l, int r){
        while(l<=r){
            if (!isalnum(s[l])) l++;
            if( !isalnum(s[r]))r--;
            if(s[l]!=s[r])
                return false;
            else{
                l++;
                r--;
            }
        }
        return true;
    }
public:
    bool validPalindrome(string s){
        int l=0,r=s.size()-1;
        transform(s.begin(),s.end(),s.begin(),::tolower);
        while(l<=r){
            if(!isalnum(s[l]))l++;
            if(!isalnum(s[r]))r--;
            if(s[l]!=s[r]){
                if(validSub(s,l+1,r) || validSub(s,l,r-1))
                    return true;
                else
                    return false;
            }
            else{
                l++;
                r--;
            }
        }
