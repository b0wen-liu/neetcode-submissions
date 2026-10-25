class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            dupes = set()
            for item in row:
                if not item == '.' and item in dupes:
                    return False
                dupes.add(item)
        for i in range(9):
            dupes = set()
            for j in range(9):
                item = board[j][i]
                if not item == '.' and item in dupes:
                    return False
                dupes.add(item)
        for i in range(3):
            for j in range(3):
                inp = []
                dupes = set()
                for k in range(i * 3, i * 3 + 3):
                    for l in range(j * 3, j * 3 + 3):
                        item = board[k][l]
                        if not item == '.' and item in dupes:
                            return False
                        dupes.add(item)
                        inp.append(item)
                # self.debug(inp)
            
        return True
    def debug(self, inp: List[int]):
        print(inp[0:3])
        print(inp[3:6])
        print(inp[6:9])