# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:48:08 2021

@author: asus
"""

##Find All Numbers Disappeared in an Array

'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ##邏輯 :
        
        ##先把list轉成set(會去除重複元素，並且排序)，並記錄原本list元素數量
        ##進行迴圈(1,number+1)，
        ##如果迴圈數字沒有在list中，則append進去
        
        
        
        
        number = len(nums) ##list元素數量
        
        nums = set(nums) ##去除重複的元素

        output = []
        
        
        
        for i in range(1,number+1):
            
            if i not in nums:
              
                output.append(i)
                

        return output