# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:31:20 2021

@author: asus
"""


##Third Maximum Number

'''

Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

'''


def thirdMax():
        """
        :type nums: List[int]
        :rtype: int
        """
        nums =[1,1,2]
        count_=2
        
        dup = sorted(nums)
        
        dup.reverse()
        
        max_num = dup[0]
        
        
        ##邏輯 
        
        ##如果list元素數量少於3，直接return 最大那個元素
        ##否則做迴圈，把list元素跑一遍，並且用count_紀錄找到多少數字
        ##如果count_歸零，表示找到第三大的數字
        ##如果count_沒歸零，則return 最大數字
        
        
        if len(dup)<3:
            return max_num
        else:
            for i in dup:
                
                if i < max_num:

                    max_num=i
                    count_-=1
                if count_==0:
                    break
        if count_!=0:
            
            return dup[0]
        
        return max_num


max_num = thirdMax()
print(max_num)