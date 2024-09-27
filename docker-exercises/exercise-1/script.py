"""
Commands used:
    pip install pyscreenshot

    when running use -v flag.
    docker run -v /path/to/host/output:/app/output
"""
import os
import sys 
import pyscreenshot
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def put_watermark(draw, x, y, text, font):
    draw.text((x, y), text, font=font)

def set_up_text(draw, xy, text, font):
     draw.text(xy, text, font=font)


def image_draw():
    try:
        img = Image.open("transposed.jpg")
        width, height = img.size
        
        draw = ImageDraw.Draw(img)
        text = "SCREENSHOT"
        
        try:
            font = ImageFont.truetype('arial.ttf', 40)
        except IOError:
            font = ImageFont.load_default()
        
        # Setting up text
        set_up_text(draw, (10, 10), text, font)

        # Calculate the coordinates for watermark
        x = 100
        y = 50

        # Put watermark
        put_watermark(draw, x, y, text, font)

        
        img.save('/app/output/watermarked.jpg')  

    except IOError as e:
        print(f"Error opening or processing the image: {e}")
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





    
