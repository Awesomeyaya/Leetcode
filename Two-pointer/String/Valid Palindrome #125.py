'''
Based on the requirements, one should only focus on the letters and numbers and ignore cases. 
So one can use str.isalnum() from both end to get the desired char of string.

Tips:  In the while loop, check the False case first, then continue with the regular path.  
       And do not use the else
'''
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True
    
'''
My stupid solution 
'''
import re 
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('\s',"",s)
        s = s.lower()
        list = []
        for item in s: 
            if item >= 'a' and item <='z' or item >='0' and item <= '9': 
                list.append(item)
        i = 0 
        j = len(list) - 1 
        while i <= j: 
            if list[i] != list[j]:
                return False 
            i = i+1
            j = j-1
        return True
