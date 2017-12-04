import builtins, random

for i in range(1,101):
    txt = "REDACTED"
    img = getattr(builtins, "__import__")("PIL.Image").Image
    rgb_img = img.new("RGB", (len(txt), 1), "white")
    # 1 row of pixels of text
    loaded = rgb_img.load()
    i = 0
    for ch in txt:
        ch = ord(ch)
        rand1 = random.randint(1,256) # 1 to 256 inclusive
        rand2 = random.randint(1,256)
        #rand3 = random.randint(1,256)
        #unused = (rand3/256)

        final = ch*(rand1/256)*(rand2/256)
        ## if in python2, final will be 0 unless rand1 == 256 && rand2 == 256

        loaded[i,0] = (rand1, rand2, round(final*10))
        i += 1
    rgb_img.save("out"+str(i)+".png")
