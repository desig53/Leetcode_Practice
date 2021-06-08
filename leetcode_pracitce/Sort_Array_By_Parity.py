# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:21:04 2021

@author: asus
"""

##Sort Array By Parity

'''
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
'''


class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
    
        ###邏輯，把偶數元素跟奇數元素互換

        length = len(nums) ##nums長度

        left = 0 
        right = length-1 

        while left<right:  
            ##做迴圈，並以left和right指向左邊和右邊位置元素
            ##如果##如果左邊為奇數、右邊為偶數，則互換
            ##反之:
            ##如果左邊指到偶數，往右走
            ##如果右邊指到奇數，往左走

            if nums[left]%2==1 and nums[right]%2==0: ##如果左邊為奇數、右邊為偶數，則互換

                temp = nums[left]

                nums[left] = nums[right]
                nums[right] = temp

                right-=1
                left+=1



            else:
                if nums[left]%2==0:  ##如果左邊指到偶數，往右走
                    left+=1
                if nums[right]%2!=0: ##如果右邊指到奇數，往左走
                    right-=1
                    
        return nums













