#Given a binary array nums, return the maximum number of consecutive 1's in the array.

##找到陣列中，連續數字為1，次數最多的

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0  ##return 的值(最大長度)
        
        current_num = 0
        
        length = len(nums)  ##陣列長度
        
        for i in range(length):  ##迴圈找出數字
            
            number = nums[i]  ##數字
            
            if number==1: ##如果找到數字為1，則current_num+1
                
                current_num+=1  ##
                
                if max_num<=current_num:##如果max_num比current_num小，把max_num指定為current_num
                    max_num = current_num
            else: ##如果找到0，則current_num歸零
                current_num=0
        return max_num
