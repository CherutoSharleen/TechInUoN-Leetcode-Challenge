'''
Problem: https://leetcode.com/problems/valid-parentheses/description/
s = "()[]{}" - True
s = "(})" - False
s = ([)] - False because order has to be same () then []
'''

class Solution():
    def isValid(self, s: str) -> bool:
        # If s is empty or is an odd number
        if s is None or len(s) % 2 == 1:
            return False
        # The solution has to start with an opening parentheses.
        # No matter how many
        # Use Stack

        # HashMap
        stack = []
        pSet = {")":"(", "]":"[","}":"{"}
        #stack[-1] is the last value added in the stack

        for char in s:
            if char in pSet:
                if stack and stack[-1] == pSet[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False


    def anotherWay(self, s: str) -> bool:
        parenthesesDict = {")":"(", "]":"[","}":"{"}
        stack = []

        # a character in the string
        for char in s:
            # if the character not in the dictionary eg (
            # append to the stack
            if char not in parenthesesDict:
                stack.append(char)
            #else it is in it eg. ), check if there's something in the stack
            # if there is check if the top of the stack is equal to the value of the key eg if ) check if TOS is == to (
            # if true return top of stack
            else:
                if not stack or parenthesesDict[char] != stack[-1]:
                    return False
                stack.pop(-1)

            return len(stack) == 0 
    
        

s = "()"
sol = Solution()
sol.isValid(s)