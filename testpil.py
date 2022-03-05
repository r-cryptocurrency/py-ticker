from PIL import Image, ImageChops, ImageFont, ImageDraw
import cmc
import os

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def imggen():
    cmcdata = cmc.getcmc()
    # font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/arial.ttf",16)

    font = ImageFont.truetype("Ubuntu-B.ttf",16)

    coinimglist = []
    for root, dirs, files in os.walk("img/coins/"):
        for file in files:
            if file.endswith(".png"):
                 coinimglist.append(os.path.join(root, file))
    # print(coinimglist)
    widthlist = []
    toptenlist = []

    leaderimg = Image.new("RGBA", (400,16), (200,240,255,255))
    draw = ImageDraw.Draw(leaderimg)
    draw.text((0,0), "Rank | Coin | Market Cap | Price (USD)", (0,0,0), font=font)
    leaderimg = trim(leaderimg)
    widthlist.append(leaderimg.size[0])
    leaderimg.save("img/temp/leader.png")

    for idx,val in enumerate(cmcdata):
        if idx == 0:
            img = Image.new("RGBA", (400,16), (200,255,200,255))
        else:
            img = Image.new("RGBA", (400,16), (225,225,225,255))
        draw = ImageDraw.Draw(img)
        text = "#{} | {} | ${:,.0f} | ${:.2f}".format(val['rank'], val['symbol'], float(val['market_cap_usd']), float(val['price_usd']))
        draw.text((0,0), text, (0,0,0), font=font)
        img = trim(img)
        img.save("img/temp/{}.png".format(val['id']))
        widthlist.append(img.size[0])
        toptenlist.append(val['id'])

    x_offset = 0
    tickerimg = Image.new("RGBA", (sum(widthlist)+300,16), (255,255,255,255))
    tickerimg.paste(leaderimg, (x_offset, 0))
    x_offset += widthlist[0]

    for idx,val in enumerate(toptenlist):
        coinimg = Image.open("img/coins/unknown.png")
        for i in coinimglist:
        # print(cmcdata[idx]['id'], coinimglist[idx])
            if cmcdata[idx]['id'] in i:
                coinimg = Image.open("img/coins/{0}.png".format(cmcdata[idx]['id']))
        textimg = Image.open("img/temp/{0}.png".format(cmcdata[idx]['id']))
        # arr = np.array(coinimg)
        # print(arr)
        # coinimgbg = Image.new("RGBA", (16,16), (255,255,255,255))
        # print("Size of coinimg is {}, and size of coinimgbg is {}".format(coinimg.size, coinimgbg.size))
        # print("Mode of coinimg is {}, and mode of coinimgbg is {}".format(coinimg.mode, coinimgbg.mode))
        # coinimg = Image.alpha_composite(coinimgbg, coinimg)
        tickerimg.paste(coinimg, (x_offset+10, 0))
        tickerimg.paste(textimg, (x_offset+26, 0))
        x_offset += widthlist[idx+1] + 26
    tickerimg.save("img/temp/ticker.png")
    print("Ticker image size = {}".format(tickerimg.size))
