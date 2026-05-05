class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1   # 0, 7

        while l < r:
            capacity = (r - l) * min(heights[l] , heights[r]) # (7 - 0) * (1, 6) -> 7*1 -> 7
            res = max(capacity, res)

            if heights[l] > heights[r]:
                r -= 1
            
            else : 
                l += 1

        return res