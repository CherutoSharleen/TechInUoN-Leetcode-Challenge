'''
The Problem involves checking if a list of numbers contains a duplicate of the same number 
eg. [1,2,3,3] - True
[1,2,3] - False
'''


from typing import List #For Type Hinting in Python 3

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # My Optimum solution
        # Using a set
        self.usingSet(nums)
        # Hashing
        self.usingHashMap(nums)
        #Sorting and comparing values
        self.usingSorting(nums)
        #Brute Force
        self.bruteForce(nums)

        print(f"\n\nThe solution is {self.usingSet(nums)} using a set\nIt is {self.usingHashMap(nums)} using a hash map\n"
        f"It is {self.usingSorting(nums)} using Sorting\nIt is {self.bruteForce(nums)} using BruteForce Solution\n\n")

    '''
    Use 2 For loops
    '''
    def bruteForce(self, nums:List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    '''
    Sorting the Numbers and then comparing the previous number and the next if similar
    '''
    def usingSorting(self, nums: List[int]) -> bool:
        #O(n) extra space O(n) time
        # Time complexity is O(n) for internal Python sort(Tim sort)
        nums_sorted = sorted(nums)
        for pos in range(len(nums_sorted)-1):
            if nums_sorted[pos] == nums_sorted[pos+1]:
                return True
        return False
    
    '''
    Using a Map: If number is seen add to the set. If it is seen again return True
    '''
    def usingHashMap(self, nums:List[int]) -> bool:
        # O(n) extra space O(n) time
        nums_map = set()
        for num in nums:
            if num in nums_map:
                return True
            nums_map.add(num)
        return False

    '''
    Set: stores unique values: no duplicates
    If the length of a set not same to length of the array, there are duplicates
    '''
    def usingSet(self, nums:List[int]) -> bool:
        # O(n) :  time O(n): Space because of the set
        set_nums = set(nums)
        if len(set_nums) != len(nums):
            return True
        return False

nums = [1,2,3,1]

sol = Solution()
sol.containsDuplicate(nums)