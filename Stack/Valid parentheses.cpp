class Solution {
public:
    bool isValid(string s) {
        vector<char> checker;
        unordered_map<char,char> bracs;
        int flag=0;
        bracs['(']=')';
        bracs['{']='}';
        bracs['[']=']';
			
        for(int i=0;i<s.size();i++){
            if(bracs.find(s[i])!=bracs.end()){
                checker.push_back(s[i]);
            }
            else{
                if(checker.empty())return false;
                char current=checker.back();
                if(s[i]==bracs[current])
                    checker.pop_back();
                else return false;
            }
            
        }
        return checker.empty();
    }
};

// Leetcode link :https://leetcode.com/problems/valid-parentheses/
