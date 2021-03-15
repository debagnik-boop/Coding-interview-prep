Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, 
such that the container contains the most water.

Sample I/O:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1,p2,max_area=0,len(height)-1,0
        while (p1<p2):
            if height[p1]<=height[p2]:
                area=height[p1]*(p2-p1)
                max_area=max(area,max_area)
                p1+=1
            else:
                area=height[p2]*(p2-p1)
                max_area=max(area,max_area)
                p2-=1
        return max_area
# Udemy Course lesson 11-17
# Leetcode problem Link: https://leetcode.com/problems/container-with-most-water/