from typing import List


class Solution:
    def bruteForce(self, nums: List[int]) -> int:
        # Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        for i in range(1, len(nums)+1):
            if i not in nums:
                return i
        return len(nums) + 1

        # Using Hash Map

    def usingHashMap(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        values = {}
        for num in nums:
            values[num] = 1
        for i in range(1, len(nums)+1):
            if i not in values:
                return i
    
    def usingSorting(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
       nums = sorted(nums)
       for i in range(len(nums)-1):
            if nums[i] < 0:
                nums[i] = 0 
            if nums[i+1] - nums[i] > 1:
                return nums[i] + 1
            return nums[-1] + 1
            
    
    def usingSet(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        numsSet = set(nums)
        for i in range(1,len(nums)+1):
            if i not in numsSet:
                    return i
            return i+1
    
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums is None or max(nums)<1:
            return 1
        
        # return self.bruteForce(nums)
        # return self.usingHashMap(nums)
        return self.usingSorting(nums)
        # return self.usingSet(nums)
       




       
    
sol = Solution()
nums = [3,4,-1,1]
# print(sol.firstMissingPositive(nums))
print(set([0,2,7,1,2,4]))