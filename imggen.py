from PIL import Image, ImageChops, ImageFont, ImageDraw
import cmc
import os

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    print(bbox)
    if bbox:
        # return im.crop(bbox)
        return im.crop((bbox[0], 0, bbox[2], 18))

def imggen(cmcdata):

    tickerimg = Image.new("RGBA", (64,640), (255,255,255,255))

    for idx,val in enumerate(cmcdata):
        coinimg = Image.open("img/newcoin/unknown.png")
        try: 
            print("Attempting to add picture of {}".format(val["slug"]))
            coinimg = Image.open("img/newcoin/{}.png".format(val["slug"]))
        except:
            pass 
        tickerimg.paste(coinimg, (0, idx*64))
    tickerimg.save("img/temp/ticker.png")
    print("Ticker image size = {}".format(tickerimg.size))
    return tickerimg
