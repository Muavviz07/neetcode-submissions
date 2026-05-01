class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hm = {}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                section = str((i)//3)+str((j)//3)
                row = str(i)+'r'
                column = str(j)+'c'

                if row not in hm:  # row level check
                    hm[row] = {val}
                else:
                    if val in hm[row]:
                        return False
                    hm[row].add(val)

                if column not in hm:  # column level check
                    hm[column] = {val}
                else:
                    if val in hm[column]:
                        return False
                    hm[column].add(val)

                if section not in hm:
                    hm[section] = {val}
                else:
                    if val in hm[section]:
                        return False
                    hm[section].add(val)

        return True