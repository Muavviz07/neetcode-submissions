class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for i in s:
            if not i.isalnum():
                continue
            t+=i.lower()
        s =t 
        #print(s)
        right = len(s)-1
        for left in range(len(s)//2):
            if s[left] != s[right]:
                return False
            right -= 1

        return True