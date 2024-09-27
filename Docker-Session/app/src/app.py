import PIL.Image
import random
import sys
 
img_flag = True
path = './pclub.png'
 
try:
    img = PIL.Image.open(path)
    img_flag = True
except:
    print(path, "Unable to find image ")

width, height = img.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))
img = img.convert('L')
chars = ["P", "B", "0", "u", "b", "P", ".", "L", "c", ",", "."]
pixels = img.getdata()
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)
 
# split string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)

for i in ".....":
    print()


for i in "."* (int(sys.argv[1]) if len(sys.argv)>1 else 1):
    with open('foo.txt','r') as f:
        t=f.read()
        lines = t.splitlines()
        print(random.choice(lines))
