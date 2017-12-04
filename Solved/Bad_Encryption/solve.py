from PIL import Image
import string

# dimension of png = 38x1
text = [['?'] for i in range(38)]

def solve():
    for i in range(100):
        filename = "out"+str(i+1)+".png"
        im = Image.open("./encoded/" + filename)
        im = im.convert('RGB')

        print(filename, im.size)

        for x in range(im.size[0]):
            for ch in string.printable:
                ch = ord(ch)
                pixel = im.getpixel((x, 0))
                rand1 = pixel[0]
                rand2 = pixel[1]
                final = ch*(rand1/256)*(rand2/256)

                if round(final*10) == pixel[2]:
                    ch = chr(int(ch))
                    text[x].append(ch)

    flag = ''

    # get most common pixels
    from collections import Counter
    for pos in text:
        count = Counter(pos)
        flag += count.most_common()[0][0]

    print(flag)

solve()         
