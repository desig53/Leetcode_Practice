#Find Numbers with Even Number of Digits


'''
Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.


Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
'''

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = []   ##
        
        digit = 1
        
        output = 0
        
##每一個數字做while迴圈，不斷除以10，
##每次除以10，則digit+1
##當這個數字除以10為0時，則迴圈break，得到最後digit，即是幾個位數
##接者判斷digit是否為偶數(除以2的餘數為0)
        
        for number in nums: 
            
            n = number
            
            digit = 1
            
            while n//10!=0:
                
                digit+=1
                
                n = n//10

            if digit%2==0:
                
                output+=1
                
            
        return output
            
