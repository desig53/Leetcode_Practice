# -*- coding: utf-8 -*-
"""
Created on Sun May 30 15:25:22 2021

@author: asus
"""
##Duplicate Zeros

'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
'''

##使用pop的概念，做迴圈，遇到0則補0，補完要pop1個元素出去

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        length = len(arr)
        
        if 0 in arr:
            
            for i in range(length-1,-1,-1):
                
                if arr[i]==0:
                    
                    arr.insert(i+1,0)
                    arr.pop()
        
        
        
        print(arr)         
                    
                    
x = Solution()
arr = [1,0,2,3]
i = x.duplicateZeros(arr)
                    
                    
                    