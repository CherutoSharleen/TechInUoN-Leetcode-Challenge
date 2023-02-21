'''
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once. eg. rat and tar
'''

class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
      # check for length can't be anagram if they are not equal
        if len(s) != len(t):
            return False
        usingHashMap(s,t)
        

        
        
# compare sorted
# Tim sort: Python O(n)
def sortBothStrings(self, s: str, t:str) -> bool:
  return sorted(s) == sorted(t)


# use a dictionary, seen{} in the first string, seen{} in the second word O(n) traversing the entire word then O(n) store O(1) access
# s and t : lowercase
def usingHashMap(self, s: str, t:str) -> bool:
  seenChars = {}
  for char in s:
     if char not in seenChars:
        seenChars[char] = 1
      else:
        seenChars[char] += 1

  for char in t:
     if char not in seenChars or seenchars[char] == 0 :
        return False
      else:
        seenChars[char] -= 1
 return True
   
