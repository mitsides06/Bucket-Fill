from bucket_fill import fill, show_image, load_image

def test_pattern():
    small_sized = load_image("data/1x1.txt")
    mid_sized = load_image("data/7x15.txt")
    large_sized = load_image("data/25x25.txt")

    #check seed_points outside image
    print()
    print("Tests if the function fill() returns input image if the seed_point inputs are outside the image.\nWe execpt the function to return the input image in all four tests below!")
    print()
    print("Before filling: ")
    show_image(mid_sized)
    print("-" * 25)
    print("After filling:")
    image_left = fill(image=mid_sized, seed_point=(2, -1))
    assert image_left == mid_sized
    image_right = fill(image=mid_sized, seed_point=(2, 15))
    assert image_right == mid_sized
    image_up = fill(image=mid_sized, seed_point=(-1, 3))
    assert image_up == mid_sized
    image_down = fill(image=mid_sized, seed_point=(7, 3))
    assert image_down == mid_sized
    show_image(image_left)
    print()
    show_image(image_right)
    print()
    show_image(image_up)
    print()
    show_image(image_down)
    print()
    print("Well done! All outside-image tests passed!")
    print()
    #check seed_points on boundaries
    print("Tests if the function fill() returns the input image when the seed_point is on a boundary.\nWe exepct our function to return the input image!")
    print()
    print("Before filling: ")
    show_image(mid_sized)
    print("-" * 25)
    print("After filling:") 
    image_boundary = fill(image=mid_sized, seed_point=(1, 5))
    assert image_boundary == mid_sized
    show_image(image_boundary)
    print()
    print("Well done! Boundary test passed!\n")
    #check non-integer inputs
    print("Tests if the function fill() returns the input image when the seed_point does not contain only integers.\nWe expect our function to return the input image in the two tests below!")
    print()
    print("Before filling: ")
    show_image(mid_sized)
    print("-" * 25)
    print("After filling:")
    image_int_1 = fill(image=mid_sized, seed_point=(3, 4.54))
    assert image_int_1 == mid_sized
    image_int_2 = fill(image=mid_sized, seed_point=(2, 'HEY'))
    assert image_int_2 == mid_sized
    show_image(image_int_1)
    print()
    show_image(image_int_2)
    print()
    print("Well done! All non-integer tests passed!\n")
    #check small-sized image
    print("Tests if the function fill() fills in an image of size 1x1 with no boundary.\nWe expect the function to return a coloured 1x1 image!\n")
    print("Before filling:\n")
    show_image(small_sized)
    print("-" * 25)
    print("After filling:\n")
    image_coloured = fill(image=small_sized, seed_point=(0, 0))
    image_coloured_test = load_image("data/1x1_test.txt")
    assert image_coloured == image_coloured_test
    show_image(image_coloured)
    print()
    print("Well done! 1x1 test passed!\n")
    #check mid-sized image
    print("Tests if the function fill() returns the correct image when a valid seed_point is input on a mid-sized image\n")
    print("Before filling: ")
    show_image(mid_sized)
    print("-" * 25)
    print("After filling:") 
    image_mid_correct = fill(image=mid_sized, seed_point=(5, 4))
    image_mid_correct_test = load_image("data/7x15_test.txt")
    assert image_mid_correct == image_mid_correct_test
    show_image(image_mid_correct)
    print()
    print("Well done! The mid_sized correct test passed!\n")
    #check large-sized image (25x25)
    print("Tests if the function fill() returns the correct image when a valid seed_point is input on a large-sized (25x25) image\n")
    print("Before filling: ")
    show_image(large_sized)
    print("-" * 25)
    print("After filling:") 
    image_large_correct = fill(image=large_sized, seed_point=(11, 14))
    image_large_correct_test = load_image("data/25x25_test.txt")
    assert image_large_correct == image_large_correct_test
    show_image(image_large_correct)
    print()
    print("Well done! The large-sized correct test passed!\n")





if __name__ == '__main__':
    # This is just an example. Feel free to change this to whatever suits you.
    test_pattern()
