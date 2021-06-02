# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:33:35 2021

@author: asus
"""


##Valid Mountain Array

'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
'''

##確認陣列是否有一個山峰，且左右為嚴格遞增與遞減

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ##分左右邊，分別往右、往左走，最後如果都到同樣位置，則reutrn true
        
        right = len(arr)-1 
        left = 0
        
        
        
        for i in range(1,len(arr)):  ##往右走，如果遞增則right+1
            
            if arr[i]>arr[i-1]:
                
                left+=1
            else:
                break
               
        for i in range(len(arr)-1,0,-1):  ##往左走，如果遞減則left-1
            
            if arr[i]<arr[i-1]:
                
                right-=1
            else:
                break
        
        return right==left and right!=0 and right!=len(arr)-1