# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:08:08 2021

@author: asus
"""
##Check If N and Its Double Exist

'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
 

Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
'''


##找到陣列中兩數，當某一數為另一數的兩倍時，則return True

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        output=False ##預設布林值為false
        
        length = len(arr) ##array長度
        
        cur = 0 #起始位置
        
        pos = 0 ##轉換位置(和cur比較)，當cur固定，則pos不斷轉換位置與cur做比較
        
        while cur<length: ##while迴圈: cur每次迴圈完畢會換新位置
            
            first = arr[cur] ##當前位置的數字，要與浮動的位置，數字做比較
            
            for i in range(0,length): ##for 迴圈，得到second，與first比較，判斷是否為兩倍
                
                if i!=cur:
                    
                    second = arr[i]
                    
                    if second*2==first  or first*2==second:
                        return True
            cur+=1 ##當前位置+1
        
        return output







