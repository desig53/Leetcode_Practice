# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:03:38 2021

@author: asus
"""


##Replace Elements with Greatest Element on Right Side

'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 105


'''



def replaceElements(self, arr):
    
        '''
        邏輯 : 
           
        從最後一個元素開始跑，先預設最大元素(maximum)為最後一個元素
        假設跑到的元素比最大元素小，則把這個值換成maximum
        假設跑到的元素筆最大元素大，則把這個值換成原本maximum，並將maximum改為跑到的這個數
            
        '''
        
        
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        great_pos = len(arr)-1 ##最大值的位置(預設最大元素(maximum)為最後一個元素)
        great_num = arr[great_pos] ##最大值
        
        for i in range(great_pos,-1,-1): ##從最後一個元素開始跑 
            
            if i==great_pos:##如果是最一個元素，把這個元素指定為-1
                arr[i]=-1
            
            
            else:
                
                
                if arr[i]<great_num:  #假設跑到的元素比最大元素小，則把這個值換成maximum
                    arr[i]=great_num
                else:  #假設跑到的元素筆最大元素大，則把這個值換成原本maximum，並將maximum改為跑到的這個數
                    temp = arr[i]
                    arr[i]=great_num
                    great_num=temp
        return arr
                    
                    
        















