
//problem link: https://leetcode.com/problems/longest-turbulent-subarray/

class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int maxLen=0,len=0;
        for(int k=0;k<arr.size();k++){
            if(k>=2 and(arr[k-2]>arr[k-1]) and (arr[k-1]<arr[k])) len++;
            else if (k>=2 and(arr[k-2]<arr[k-1]) and (arr[k-1]>arr[k])) len++;
                // cout<<k<<endl;
                // cout<<"len"<<" "<<len<<endl;
                // cout<<"max"<<" "<<maxLen<<endl;
            else if(k>=1 and arr[k]!=arr[k-1]){
                len=2;
                // cout<<k<<endl;
                // cout<<len<<endl;
            }
            else{
                len=1;
                // cout<<k<<endl;
                // cout<<len<<endl;
            }
            maxLen=max(maxLen,len);
        }
        return maxLen;
    }
};
