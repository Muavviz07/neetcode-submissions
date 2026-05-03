class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        if len(numbers) == 2:
            return [1,2]
        for i in range(len(numbers)):
            if numbers[i] not in hmap: # 3-1 , 
                hmap[target-numbers[i]] = i   # {2: 0, } 
                continue
            
            return ([hmap[numbers[i]]+1,i+1])