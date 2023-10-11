""" Coursework 1: Bucket Fill
"""

def load_image(filename):
    """ Load image from file made of 0 (unfilled pixels) and 1 (boundary pixels) and 2 (filled pixel)

    Example of content of filename:

0 0 0 0 1 1 0 0 0 0
0 0 1 1 0 0 1 1 0 0
0 1 1 0 0 1 0 1 1 0
1 1 0 0 1 0 1 0 1 1
1 0 0 1 0 0 1 0 0 1
1 0 0 1 0 0 1 0 0 1
1 1 0 1 0 0 1 0 1 1
0 1 1 0 1 1 0 1 1 0
0 0 1 1 0 0 1 1 0 0
0 0 0 0 1 1 0 0 0 0

    Args:
        filename (str) : path to file containing the image representation

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel
               2 represents a filled pixel
    """

    image = []
    with open(filename) as imagefile:
        for line in imagefile:
            if line.strip():
                row = list(map(int, line.strip().split()))
                image.append(row)
    return image


def stringify_image(image):
    """ Convert image representation into a human-friendly string representation

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)

    Returns:
        str : a human-friendly string representation of the image
    """
    
    if image is None:
        return ""

    # The variable "mapping" defines how to display each type of pixel.
    mapping = {
        0: " ",
        1: "*",
        2: "0"
    }

    image_str = ""
    if image:
        image_str += "+ " + "- " * len(image[0]) + "+\n"
    for row in image:
        image_str += "| "
        for pixel in row:
            image_str += mapping.get(pixel, "?") + " "
        image_str += "|"
        image_str += "\n"
    if image:
        image_str += "+ " + "- " * len(image[0]) + "+\n" 
        
    return image_str


def show_image(image):
    """ Show image in terminal

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
    """
    print(stringify_image(image))


def fill(image, seed_point):
    """ Fill the image from seed point to boundary

    the image should remain unchanged if:
    - the seed_point has a non-integer coordinate
    - the seed_point is on a boundary pixel
    - the seed_point is outside of the image

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        seed_point (tuple) : a 2-element tuple representing the (row, col) 
                       coordinates of the seed point to start filling

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel, and
               2 represents a filled pixel
    """
    if not is_seed_point_valid(image, seed_point):
        return image
    
    row_index = seed_point[0]
    col_index = seed_point[1]
    
    image[row_index][col_index] = 2      # Fill in the pixel.

    # Check if the current position is surrounded by boundaries or filled pixels.
    if is_left_boundary(image, seed_point) and is_right_boundary(image, seed_point) and\
         is_up_boundary(image, seed_point) and is_down_boundary(image, seed_point):
        return image
    
    # Call the fill fuction to each of the surrounding positions which are boundary-free and empty
    # to update the image by filling in the appropriate pixels.
    if not is_left_boundary(image, seed_point):
        new_position = (row_index, col_index-1)
        image = fill(image, new_position)
    if not is_right_boundary(image, seed_point):
        new_position = (row_index, col_index+1)
        image = fill(image, new_position)
    if not is_up_boundary(image, seed_point):
        new_position = (row_index-1, col_index)
        image = fill(image, new_position)
    if not is_down_boundary(image, seed_point):
        new_position = (row_index+1, col_index)
        image = fill(image, new_position)

    return image

def is_seed_point_valid(image, seed_point):
    """ Checks if the seed_point input is valid

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        seed_point (tuple) : a 2-element tuple representing the (row, col) 
                       coordinates of the seed point to start filling

    Returns:
        Bool : True or False                
    """
    row_dim = len(image)
    col_dim = len(image[0])
    row_index = seed_point[0]
    col_index = seed_point[1]

    # Check if the seed_point input consists only of integers, if it's positioned within the image,
    # and if it's positioned on a boundary-free pixel.
    if (type(row_index) == type(col_index) == int):
        return (0 <= row_index <= row_dim-1) and (0 <= col_index <= col_dim-1) and image[row_index][col_index] == 0
    return False
    

def is_left_boundary(image, current_pixel):
    """ Checks if the pixel to the left of the current pixel position is a boundary or already filled

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        current_pixel (tuple) : a 2-element tuple representing the (row, col)
                        cooredinates of the current pixel
    
    Returns:
        Bool : True or False
    """
    row_index = current_pixel[0]
    col_index = current_pixel[1]
    if col_index == 0:
        return True
    if image[row_index][col_index-1] in [1, 2]:
        return True
    return False

def is_right_boundary(image, current_pixel):
    """ Checks if the pixel to the right of the current pixel position is a boundary or already filled

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        current_pixel (tuple) : a 2-element tuple representing the (row, col)
                        cooredinates of the current pixel
    
    Returns:
        Bool : True or False
    """

    col_dim = len(image[0])
    row_index = current_pixel[0]
    col_index = current_pixel[1]
    if col_index == col_dim - 1:
        return True
    if image[row_index][col_index+1] in [1, 2]:
        return True
    return False

def is_up_boundary(image, current_pixel):
    """ Checks if the pixel above the current pixel position is a boundary or already filled

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        current_pixel (tuple) : a 2-element tuple representing the (row, col)
                        cooredinates of the current pixel
    
    Returns:
        Bool : True or False
    """
    row_index = current_pixel[0]
    col_index = current_pixel[1]
    if row_index == 0:
        return True
    if image[row_index-1][col_index] in [1, 2]:
        return True
    return False

def is_down_boundary(image, current_pixel):
    """ Checks if the pixel below the current pixel position is a boundary or already filled

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        current_pixel (tuple) : a 2-element tuple representing the (row, col)
                        cooredinates of the current pixel
    
    Returns:
        Bool : True or False
    """
    row_dim = len(image)
    row_index = current_pixel[0]
    col_index = current_pixel[1]
    if row_index == row_dim - 1:
        return True
    if image[row_index+1][col_index] in [1, 2]:
        return True
    return False





    



def example_fill():
    image = load_image("data/smiley.txt")

    print("Before filling:")
    show_image(image)

    image = fill(image=image, seed_point=(1, 3))

    print("-" * 25)
    print("After filling:")
    show_image(image)


if __name__ == '__main__':
    example_fill()

