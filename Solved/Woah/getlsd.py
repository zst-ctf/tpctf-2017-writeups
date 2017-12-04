#!/usr/bin/env python3
from PIL import Image

im = Image.open('meme.png')
im = im.convert('RGB')

flag = ''
for x in range(im.size[0]):
	pixel = im.getpixel((x, 0))
	flag += str(pixel[0] & 1)
	flag += str(pixel[1] & 1)
	flag += str(pixel[2] & 1)

print(flag)