#Find Numbers with Even Number of Digits

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = []
        
        digit = 1
        
        output = 0
        
        for number in nums:
            
            n = number
            
            digit = 1
            
            while n//10!=0:
                
                digit+=1
                
                n = n//10

            if digit%2==0:
                
                output+=1
                
            
        return output
            
