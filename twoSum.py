class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res,ind,i={},[],0
        while i<len(nums):
            p1=nums[i]
            rem=target-p1
            if rem in res:
                ind.append(res[rem])
                ind.append(i)
                return ind
            else:
                res[nums[i]]=i
                i+=1
        return ind
        
#Udemy Course Lesson 1-9
# LeetCode Link: https://leetcode.com/problems/two-sum/