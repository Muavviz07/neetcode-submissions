class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hm = {}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                section = str((i)//3)+str((j)//3) # 00 or 01 or 02 or 10 or 11 or 12
                row = str(i)+'r'
                column = str(j)+'c'

                if row not in hm: # row level check
                    hm[row] = [val]
                else:
                    if val in hm[row]:
                        return False
                    hm[row].append(val)

                if column not in hm: # Column Level check
                    hm[column] = [val]
                else:
                    if val in hm[column]:
                        return False
                    hm[column].append(val)

                if section not in hm:
                    hm[section] = [val]
                else:
                    if val in hm[section]:
                        return False
                    hm[section].append(val) 

        return True