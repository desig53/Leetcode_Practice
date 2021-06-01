# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:53:07 2021

@author: asus
"""
#Merge Sorted Array

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. 
You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.


Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
'''

##把nums2元素放到nums1做排序


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        total = m+n-1  ##nums1總共包含的空間
        
        p1 = m-1 ##nums1元素數量
        
        p2 = n-1  ##nums2元素數量
        

        while p1>=0 and p2>=0:  
            
            ##1.做while迴圈，將nums1[p1]與nums2[p2]做比較
            ##2.如果nums1[p1]比nums2[p2]大，則把nums1[total]給予nums1[p1]
            ##2.反之，把nums[p2]給予nums1[p1]
            ##3.最後，再做一個while迴圈，把p2多餘元素放入nums2中
            
            ##比較nums1、nums2
            if nums1[p1]>nums2[p2]:
                
                nums1[total]=nums1[p1]
                
                p1-=1
                
            elif nums1[p1]<=nums2[p2]:
                
                nums1[total]=nums2[p2]
                
                p2-=1
                
            total-=1
            
         
        while p2>=0:
            
            nums1[total]=nums2[p2]
            total-=1
            p2-=1
            
        
        print()
        print(nums1)

nums1 = [2,0]

m = 1

nums2 = [1]


n = 1

x = Solution()

x.merge(nums1,m,nums2,n)

