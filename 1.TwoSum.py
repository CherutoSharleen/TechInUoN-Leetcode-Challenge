from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #BruteForce
        # self.bruteForce(nums, target)
        # Using Hash Map

        values = {}
        for pos, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [values[diff],pos]
            else:
                values[num] = pos 
        
    def bruteForce(self, nums:List[int], target: int) -> List[int]:
        for first_num in range(len(nums)):
            for second_num in range(first_num+1, len(nums)):
                if nums[first_num] + nums[second_num] == target:
                    return [first_num, second_num]
    

           
sol = Solution()
nums = [2,7,11,15]
target = 9
answer = sol.twoSum(nums, target)
print(answer)

            
        