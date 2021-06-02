# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:12:54 2021

@author: asus
"""


##Remove Duplicates from Sorted Array

'''
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]

Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            
            return 0
        
        
        dup = 1 ##要蓋過的位置
        
        length = 1 ##長度
        
        number = nums[0] ##當前數字
        
        for i in range(1,len(nums)): ##迴圈
            
            if nums[i]!=number:  
                
                ##如果遇到不同數字:
                ##1.把當前位置的數字蓋過(被新數字蓋過)
                ##2.更新下一個當前數字
                ##3.當前位置更新
                ##4.長度+1
                
                
                
                nums[dup]=nums[i]
                
                number = nums[i]
                
                dup+=1
                
                length+=1
                
        return length