# ================================UMPIRE========================================
# Understand :
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.
#
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#
# For example, inverting [0,1,1] results in [1,0,0].
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output:        [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

# Match:
# Maximum 2    2D List

# Implementation :
def flipAndInvertImage(image):
    # Flip and invert each row
    for i in range(len(image)):
        # Reverse the row
        image[i] = image[i][::-1]
        # Invert the row
        image[i] = [1 - x for x in image[i]]
    return image


# Example usage
image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
flipped_and_inverted_image = flipAndInvertImage(image)

print(flipped_and_inverted_image)
# Output: [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
