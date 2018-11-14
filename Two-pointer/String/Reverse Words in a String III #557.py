'''

Tips: 
1. split the sentence in the right way 
2. transfer each word(string) to list 
For each word, use the reverse function 
3. remember to add space after each word
4. delete the extra space at the end 

'''

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        str = []
        for item in s:
            str.append(self.reverse(item))
            str.append(' ')
        return "".join(str).strip()
        
            
    def reverse(self,item):
        item = list(item)
        i = 0 
        j = len(item) - 1
        while i<= j: 
            item[i],item[j] = item[j],item[i]
            i = i+1 
            j = j-1
        return "".join(item)
