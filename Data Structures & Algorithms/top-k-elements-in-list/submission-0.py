class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1

        # print(sorted(my_dict, key=my_dict.get))
        st = sorted(dic, key=dic.get, reverse = True)

        return(st[:k])