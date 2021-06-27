from matplotlib import pyplot
import numpy
import random

def get_color_decimal_code():
    return random.randint(255)

def get_pixel():
    pixel_color = []
    for i in range(2):
        pixel_color.append(get_color_decimal_code())
    return pixel_color

def get_image_row(size=32):
    image_row = []
    for i in range(size-1):
        image_row.append(get_pixel())
    return image_row

def get_full_image():
    full_image = []
    for i in range (len(get_image_row(size=32)-1)):
        full_image.append(get_image_row(size=32))
    return full_image

def convert_to_numpy_array(arr):
    return numpy.array(arr) 

def show_random_image():
    pyplot.imshow(convert_to_numpy_array(get_full_image))

show_random_image()


