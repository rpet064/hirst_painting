#! Python 3
#colorgram.py
#this file extracts colors from image into tuple - to be used in hirst_painting file

import colorgram
rgb_colors = []
color_tup = colorgram.extract("image.jpg.jpg", 10)
for color in color_tup:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)