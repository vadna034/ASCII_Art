from PIL import Image
from PIL import ImageStat
import numpy as np
import math
import sys



def getGreyscaleImage(url):
    try:
        return Image.open(url).convert('L')
    except:
        print("INVALID/NO IMAGE PATH INPUT")
        exit(1)


def getBrightness(image):

    stat = ImageStat.Stat(image)
    return stat.rms[0]

def generateBrightnessArray(image, rows):
    assert type(rows) == int

    width, height = image.size[0], image.size[1]
    columns = round(width / height * rows) * 2
    height_section = width / rows
    width_section = height / columns
    row_brightness = []

    for i in range(rows):
        y1 = int(height_section * i)
        y2 = int(y1 + height_section)
        row = []
        for j in range(columns):
            x1 = int(width_section * j)
            x2 = int(x1 + width_section)
            testImage = image.crop([x1, y1, x2, y2])
            row.append(getBrightness(testImage))
        row_brightness.append(row)
    return row_brightness

def outputToFile(brightnessArray, gScale, outputFile):
    output = open(outputFile, 'w')
    for row in brightnessArray:
        for char in row:
            index = round((char / 255) * len(gScale))
            output.write(gScale[index - 1])
        output.write('\n')
    output.close()


def main(inputURl, rows, outputFile, gScale):
    if gScale == 1:
        gScale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. " #70 level greyscale
    elif gScale == 2:
        gScale = "@%#*+=-:, "  # 10 level greyscale inverted
    elif gScale == 3:
        gScale = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"  # 70 level greyscale inverted
    else:
        gScale = " .:-=+*#%@"  # 10 level greyscale
    greyImage = getGreyscaleImage(inputURl)
    brightnessArray = generateBrightnessArray(greyImage, rows)
    outputToFile(brightnessArray, gScale, outputFile)
    greyImage.close()


if len(sys.argv) == 2:
    main(sys.argv[1], 50, "Output.txt", 1)
elif len(sys.argv) == 3:
    main(sys.argv[1], int(sys.argv[2]), "Output.txt", 1)
elif len(sys.argv) == 4:
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3], 1)
else:
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4]))
