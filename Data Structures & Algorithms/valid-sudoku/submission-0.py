class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Map number string ("1" to "9") -> [seen_rows, seen_cols, seen_submats]
        coords = {str(digit): [set(), set(), set()] for digit in range(1, 10)}

        for i in range(9):
            for j in range(9):
                item = board[i][j]

                # 1. Skip empty cells
                if item == ".":
                    continue

                # 2. Formula to calculate 3x3 box index (0 through 8)
                submat = (i // 3) * 3 + (j // 3)

                # 3. Check for collisions in row, col, or 3x3 box
                if (
                    i in coords[item][0]
                    or j in coords[item][1]
                    or submat in coords[item][2]
                ):
                    return False

                # 4. Record coordinates
                coords[item][0].add(i)
                coords[item][1].add(j)
                coords[item][2].add(submat)

        return True