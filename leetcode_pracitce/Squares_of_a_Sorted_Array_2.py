# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:08:27 2021

@author: asus
"""


##Squares of a Sorted Array

'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ###解題邏輯 :
        
        ## 建立兩個指標，一個指向最大，一個指向最小
        ## 建立一個空list
        ## 用while迴圈，將原本list中元素和兩個指標指到的元素做比較，指到比較大的元素，則放進去新的list
        
        
        min_,max_ = 0,len(nums)-1 ##指標
        
        number = len(nums) ##list長度
        
        output = [0 for i in range(number)] ##最後輸出的list
        
        point = number-1
        
        while max_>=min_:
            
            if abs(nums[max_]) >= abs(nums[min_]):
                output[point] = nums[max_]**2
                max_ -=1
                
            else:
                output[point] = nums[min_]**2
                min_+=1
                
                
            point-=1
            
        
        
        
        return output