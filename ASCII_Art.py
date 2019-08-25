from PIL import Image
from PIL import ImageStat
import numpy
import math
import sys

gScale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " #70 level greyscale
gScale2 = " .:-=+*#%@" #10 level greyscale

imageUrl = sys.argv[1]
rows = int(sys.argv[2])

greyImage = Image.open(imageUrl).convert('LA')

width, height = greyImage.size[0], greyImage.size[1]
columns = round((width / height) * rows) * 2

height_section = width / columns
width_section = height / rows

row_brightness = []
for i in range(rows):
    y1 = int(height_section * i)
    y2 = int(y2 + height_section)
    for j in range(columns):
        x1 = int(width_section * j)
        x2 = int(x2 + width_section)
        testImage = greyImage.crop([x1, y1, x2, y2])
        brightness =


output = open("Output.txt", 'w')

for row in row_brightness:
    for char in row:
        index = round((char/256)*70)
        output.write(gScale1[index-1])
    output.write('\n')

output.close()

greyImage.close()


