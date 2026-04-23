class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            for j in i:
                res += chr(ord(j)+2)
            res += ' '
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        t = ''
        for i in s:
            if i == " ":
                res.append(t)
                t = ''
                pass
            else:
                t += chr(ord(i)-2)

        return res
