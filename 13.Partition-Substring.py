'''
Our task is to partition the string into one or more substrings such that the characters
in each substring are unique.

We have to return the minimum number of substrings in such a partition.

1. No letter can be repeated in a substring

s = abacaba
output = 4
Explanation: The string can be partitioned as [a, ba, cab, a] and [ab,ac,ab,a]
https://leetcode.com/problems/optimal-partition-of-string/description/

'''

# Solution
class Solution:
    def partitionString(self, s: str) -> int:
        lastSeen = [-1]*26
        count = 1
        substringStarting = 0

        for i in range(len(s)):
            if lastSeen[ord(s[i]) - ord('a')] >= substringStarting:
                count += 1
                substringStarting = i
            lastSeen[ord(s[i]) - ord('a')] = i

        return count

sol = Solution()
print(sol.partitionString('abacaba'))
        