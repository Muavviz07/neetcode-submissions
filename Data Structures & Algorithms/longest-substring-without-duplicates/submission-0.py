class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = [] # a b c  
                   #  t = 'z'
        res = 0
        for i in s:
            if i in stack:
                t = stack.pop(0)
                while t != i:
                    t = stack.pop(0)

                stack.append(i)

            else:
                stack.append(i)
            
            res = max(res, len(stack))

        return res

        