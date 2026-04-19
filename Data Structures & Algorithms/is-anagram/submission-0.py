class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for i in t:
            if i not in dic or dic[i] <= 0:
                return False
            else:
                dic[i] -= 1

        for i in dic:
            if dic[i] != 0:
                return False
        return True
