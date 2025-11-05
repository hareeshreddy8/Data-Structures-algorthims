#https://leetcode.com/problems/valid-sudoku/submissions/1821555425/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #hceck whether given list is 9 * 9
        if len(board) != 9 or any(len(row) != 9 for row in board) :
            return False 
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9) :
            for c in range(9) :
                val = board[r][c]
                if val == '.' or val == '0' :
                    continue 
                if val not in {'1','2','3','4','5','6','7','8','9'} :
                    return False
                box_index =  (r // 3) * 3 + (c // 3)
                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_index]) :
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        return True