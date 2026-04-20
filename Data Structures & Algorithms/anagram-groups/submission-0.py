class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic,res = [], []

        for i in strs:
            curr = {}
            for j in i:
                curr[j] = curr.get(j,0) + 1   # Gets Count of each Chars

            t, found = 0, False
            for j in dic:
                if j == curr:
                    res[t].append(i)
                    found = True

                t += 1
            
            if not found:
                res.append([i])
                dic.append(curr)
        return res

            