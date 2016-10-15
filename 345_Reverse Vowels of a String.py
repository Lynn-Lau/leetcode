
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        string = list(s)
        left = 0; right = length-1
        vowellist = ['a', 'e', 'i', 'o', 'u']
        while left < right:
            
            if left < right and string[left].lower() not in vowellist:
                left += 1
            if left < right and string[right].lower() not in vowellist:
                right -= 1
            if left != right:
                temp = string[left]
                string[left] = string[right]
                string[right] = temp

            left += 1; right -= 1

            return ''.join(string)

        