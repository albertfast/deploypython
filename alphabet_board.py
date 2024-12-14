'''
we have 5X6 alphabet board arranged in order:
board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
 we start at position (0, 0),
 corresponding to character board[0][0].
 'U' Move up one row(if possible).
 'D' Move down one row(if possible).
 'L' Move left one row(if possible).
 'R' Move right one row(if possible).
 '!': Select current charecter to include in the result.

 Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
from 'a' DDL ==> 'l' and we stopped with '!' then from 'l' UURRR ==> 'e' we stopped e with '!'
then one more '!' giving same elementh 'e' then form 'e' DDD ==> 't' we stopped e with '!'

we have to Return a sequence of moves that makes our answer equal to target in the minimum number of moves.
You may return any path that does so.


 board = [  a b c d e
            f g h i j
            k l m n o
            p q r s t
            u v w x y
            z ]
'''


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # Mapping each character to its position on the board
        board_map = {chr(97 + i): (i // 5, i % 5) for i in range(26)}

        # Starting position at 'a'
        current_row, current_col = 0, 0
        result = []

        for char in target:
            # Target position for the current character
            target_row, target_col = board_map[char]

            # Move up or down first (handling 'z' position carefully)
            if current_row > target_row:
                result.append('U' * (current_row - target_row))
            if current_col > target_col:
                result.append('L' * (current_col - target_col))
            if current_row < target_row:
                result.append('D' * (target_row - current_row))
            if current_col < target_col:
                result.append('R' * (target_col - current_col))

            # Append '!' to select the current character
            result.append('!')

            # Update current position
            current_row, current_col = target_row, target_col

        # Join all moves into a single string
        return ''.join(result)

