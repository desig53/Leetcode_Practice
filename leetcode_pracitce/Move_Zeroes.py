# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:10:03 2021

@author: asus
"""

##Move Zeroes

'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        pos = 0 ##0的位置(用於兩值互換)
        
        if nums == [0]: ##如果只有個0，直接return
            
            return nums
        elif nums==[1]:
            return [0]
        
        
        else:
            
            '''
            如果找到0，則先暫存這個位置
            如果找到非0，則將這個值跟左邊0的位置，兩值互換
            '''
            
            for i in range (len(nums)):
                
                if nums[i]==0: ##如果找到0，則先跳過
                    
                    continue
                
                else:  
                    ##兩值互換
                    ##下一個要換的位置+1
                    temp = nums[pos]
                    nums[pos]=nums[i]
                    nums[i]=temp
                    pos+=1
                    
                    
        return nums