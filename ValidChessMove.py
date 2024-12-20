# ================================UMPIRE========================================
# Understand:
#Given a chess piece, its starting position, and its ending position determine if its a valid chess move.
# (If you're unfamiliar with chess, you can check out

# Rooks can only move horizontally and vertically
        # Rook
        # Movement: The rook can move any number of squares horizontally or vertically.
    # Mathematics:
        # A horizontal move occurs when the y-coordinate remains the same: start_y == end_y.
        # A vertical move occurs when the x-coordinate remains the same: start_x == end_x.
        # In both cases, the rook can move an arbitrary number of squares, as long as either
        # the x or y coordinate doesn't change.
    # Examples:
        # Start: (3, 1), End: (7, 1) → This is a vertical move (start_x != end_x, but start_y == end_y).
        # Start: (5, 5), End: (5, 8) → This is a horizontal move (start_x == end_x, but start_y != end_y).

# Knights can only move in an L-shape
        # Knight
        # Movement: The knight moves in an L-shape, meaning it moves:
        # Two squares in one direction and one square in the perpendicular direction, or
        # One square in one direction and two squares in the perpendicular direction.
    # Mathematics:
        # Calculate the change in the x (dx) and y (dy) coordinates: dx = abs(start_x - end_x) and dy = abs(start_y - end_y).
        # A valid L-shape occurs when:
        # dx == 2 and dy == 1 (two steps in x-direction and one in y-direction), or
        # dx == 1 and dy == 2 (one step in x-direction and two in y-direction).
    # Examples:
        # Start: (4, 4), End: (6, 5) → dx = 2, dy = 1 → Valid L-shape move.
        # Start: (1, 1), End: (3, 2) → dx = 2, dy = 1 → Valid move.

# Bishops can only move diagonally
        # Bishop
        # Movement: The bishop can move diagonally any number of squares.
    # Mathematics:
        # A diagonal move occurs when the absolute difference between the x and y coordinates is the same:
        # abs(start_x - end_x) == abs(start_y - end_y)
        # This ensures the move maintains a consistent slope.
    # Examples:
        # Start: (1, 1), End: (3, 3) → abs(1 - 3) == abs(1 - 3) → Valid diagonal move.
        # Start: (4, 4), End: (2, 2) → abs(4 - 2) == abs(4 - 2) → Valid move.

# Queens can move diagonally or horizontally from their starting position
        # Queen
        # Movement: The queen combines the movement abilities of the rook and the bishop:
        # Horizontally, vertically, or diagonally.
    # Mathematics:
        # A queen move is valid if:
        # It moves like a rook (start_x == end_x or start_y == end_y), or
        # It moves like a bishop (abs(start_x - end_x) == abs(start_y - end_y)).
    # Examples:
        # Start: (1, 1), End: (1, 8) → Horizontal move (like a rook).
        # Start: (4, 4), End: (6, 6) → Diagonal move (like a bishop).

# Kings can move in any direction (horizontal, vertical, diagonal), but can only move 1 space
        # King
        # Movement: The king can move one square in any direction (horizontally, vertically, or diagonally).
    # Mathematics:
        # Calculate the change in the x (dx) and y (dy) coordinates: dx = abs(start_x - end_x) and dy = abs(start_y - end_y).
        # A valid move occurs when both dx and dy are at most 1:
        # dx <= 1 and dy <= 1.
    # Examples:
        # Start: (4, 4), End: (5, 5) → dx = 1, dy = 1 → Valid move.
        # Start: (1, 1), End: (1, 2) → dx = 0, dy = 1 → Valid move.


# A piece can't start and end in the same position (The piece has to move)
# Note: For now, we won't focus piece capturing, or special rules like castling. We also won't consider positions off the board,
# so you can just focus on how the pieces move.

# Example:               Input:                     Output:
#            valid_chess_move("BISHOP",1,1,8,8)      True
#            valid_chess_move("QUEEN",4,4,8,4)       True
#            valid_chess_move("KING",1,5,1,5)        False

# Match:
# - Use conditional logic to check the movement rules for each piece.
# - Calculate differences (dx and dy) to determine the move's validity.
# - Return False if the starting and ending positions are the same.

# Plan:
# 1. If the starting and ending positions are the same, return False.
# 2. For each chess piece:
#    - Rook: Check if either the x or y coordinate remains constant.
#    - Knight: Check if the move follows the L-shape pattern.
#    - Bishop: Check if the absolute difference between x and y coordinates is the same.
#    - Queen: Combine the logic for rook and bishop.
#    - King: Check if the move is within one square in any direction.
# 3. Return False for invalid inputs.

# Implementation:
def king_move(start_x, start_y, end_x, end_y):
    dx = abs(start_x - end_x)
    dy = abs(start_y - end_y)
    return dx <= 1 and dy <= 1


def bishop_move(start_x, start_y, end_x, end_y):
    return abs(start_x - end_x) == abs(start_y - end_y)


def rook_move(start_x, start_y, end_x, end_y):
    return start_x == end_x or start_y == end_y


def queen_move(start_x, start_y, end_x, end_y):
    return rook_move(start_x, start_y, end_x, end_y) or bishop_move(start_x, start_y, end_x, end_y)


def knight_move(start_x, start_y, end_x, end_y):
    dx = abs(start_x - end_x)
    dy = abs(start_y - end_y)
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


def valid_chess_move(piece, start_x, start_y, end_x, end_y):
    if start_x == end_x and start_y == end_y:
        return False

    piece = piece.upper()
    if piece == "KING":
        return king_move(start_x, start_y, end_x, end_y)
    elif piece == "BISHOP":
        return bishop_move(start_x, start_y, end_x, end_y)
    elif piece == "ROOK":
        return rook_move(start_x, start_y, end_x, end_y)
    elif piece == "QUEEN":
        return queen_move(start_x, start_y, end_x, end_y)
    elif piece == "KNIGHT":
        return knight_move(start_x, start_y, end_x, end_y)
    return False


def main():
    piece = input("Piece type (ROOK, KNIGHT, BISHOP, QUEEN, KING): ")
    start_x = int(input("Starting X coordinate (1-8): "))
    start_y = int(input("Starting Y coordinate (1-8): "))
    end_x = int(input("Ending X coordinate (1-8): "))
    end_y = int(input("Ending Y coordinate (1-8): "))

    is_valid = valid_chess_move(piece, start_x, start_y, end_x, end_y)
    print(f"Is it a valid move? {is_valid}")


if __name__ == "__main__":
    main()



# def valid_chess_move(piece, start_x, start_y, end_x, end_y):
#     """
#     Determines if a given chess move is valid based on chess piece rules.
#
#     Args:
#         piece (str): The type of chess piece (e.g., "ROOK", "KNIGHT").
#         start_x (int): Starting x-coordinate.
#         start_y (int): Starting y-coordinate.
#         end_x (int): Ending x-coordinate.
#         end_y (int): Ending y-coordinate.
#
#     Returns:
#         bool: True if the move is valid, False otherwise.
#     """
#     # If starting and ending positions are the same, the move is invalid
#     if start_x == end_x and start_y == end_y:
#         return False
#
#     # Check movement rules based on the piece type
#     if piece.upper() == "ROOK":
#         # Rook can move horizontally or vertically
#         return start_x == end_x or start_y == end_y
#
#     elif piece.upper() == "KNIGHT":
#         # Knight moves in an L-shape
#         dx = abs(start_x - end_x)
#         dy = abs(start_y - end_y)
#         return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)
#
#     elif piece.upper() == "BISHOP":
#         # Bishop moves diagonally
#         return abs(start_x - end_x) == abs(start_y - end_y)
#
#     elif piece.upper() == "QUEEN":
#         # Queen can move diagonally, horizontally, or vertically
#         return (start_x == end_x or start_y == end_y or
#                 abs(start_x - end_x) == abs(start_y - end_y))
#
#     elif piece.upper() == "KING":
#         # King can move one square in any direction
#         dx = abs(start_x - end_x)
#         dy = abs(start_y - end_y)
#         return dx <= 1 and dy <= 1
#
#     # If the piece type is not recognized, return False
#     return False
#
# # Test cases:
# def main():
#     """
#     Test the valid_chess_move function with user input.
#     """
#     # Prompt user for chess piece and coordinates
#     print("Enter the chess piece and positions.")
#     piece = input("Piece type (ROOK, KNIGHT, BISHOP, QUEEN, KING): ")
#     start_x = int(input("Starting X coordinate (1-8): "))
#     start_y = int(input("Starting Y coordinate (1-8): "))
#     end_x = int(input("Ending X coordinate (1-8): "))
#     end_y = int(input("Ending Y coordinate (1-8): "))
#
#     # Check if the move is valid
#     is_valid = valid_chess_move(piece, start_x, start_y, end_x, end_y)
#     print(f"Is it a valid move? {is_valid}")
#
# # Run the main function
# if __name__ == "__main__":
#     main()