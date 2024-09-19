"""
Commands used:
    pip install pyscreenshot
"""
import os
import sys 
import pyscreenshot
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def image_draw():
    try:
        img = Image.open("transposed.jpg")
        width, height = img.size
        
        draw = ImageDraw.Draw(img)
        
        text = "SCREENSHOT"
        font = ImageFont.truetype('arial.ttf', 40)

        draw.text((10, 10), text, font=font)

        #calc of the coordinates 
        x = 100
        y = 50

        #put watermakr
        draw.text((x, y), text, font=font)
        img.show()

        img.save('watermarked.jpg')

    except IOError as e:
        print(e)
        pass


def image_transpose():
    try:
        img = Image.open("temp.jpg")
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        transposed_img.save("transposed.jpg")
    except IOError as e:
        print(e)
        pass

def image_screenshot():
    try:
        image = pyscreenshot.grab(bbox=(20, 20, 400, 400))
        image.show()
        image.save("temp.jpg")
    except Exception as e:
        print(e)

def array_manipulation(arr):
    np_array = np.array(arr)
    np.sort(np_array)
    squared_arr = np.square(np_array)
    print(squared_arr)


if __name__ == "__main__":
    #env variable 
    greeting = os.getenv('GREETING', 'env=Hello bro!')
    print(greeting)

    # image screenshot
    #image_screenshot()

    # image operations
    #image_transpose()
    #image_draw()

    # array manipulation
    n = len(sys.argv)
    arr = []
    for i in range(1, n):
        arr.append(int(sys.argv[i]))
    
    array_manipulation(arr)





    
