import os
import requests
import glob
from PIL import Image

imgs = {
    "vs_bg": "./img/vs_bg.png",
    "vs_bg_animated": "./img/vs_bg_animated/frame_*.jpg"
}


async def vs_create(url1:str, url2:str):
    vs_bg = Image.open(os.path.join(imgs["vs_bg"]))
    

    size = (150, 150)

    fighter1 = Image.open(requests.get(url1, stream=True).raw).resize(size)
    fighter2 = Image.open(requests.get(url2, stream=True).raw).resize(size)

    pos1 = (vs_bg.width//2 - fighter1.width*2, vs_bg.height//2 - fighter1.height+80)
    pos2 = (vs_bg.width//2 + fighter2.width, vs_bg.height//2 - fighter2.height+80)

    vs_bg.paste(fighter1, pos1)
    vs_bg.paste(fighter2, pos2)



    vs_bg.save(os.path.join("./img", "result.png"))
    

async def vs_create_animated(url1:str, url2:str):
    vs_bg, *img = [Image.open(path) for path in glob.glob(imgs["vs_bg_animated"])]
    
    size = (150, 150)

    fighter1 = Image.open(requests.get(url1, stream=True).raw).resize(size)
    fighter2 = Image.open(requests.get(url2, stream=True).raw).resize(size)

    pos1 = (vs_bg.width//2 - fighter1.width*2, vs_bg.height//2 - fighter1.height+80)
    pos2 = (vs_bg.width//2 + fighter2.width, vs_bg.height//2 - fighter2.height+80)

    vs_bg.paste(fighter1, pos1)
    vs_bg.paste(fighter2, pos2)

    for im in img:
        im.paste(fighter1, pos1)
        im.paste(fighter2, pos2)

    vs_bg.save(fp=os.path.join("./img", "result.gif"), append_images=img, save_all=True, duration=20, loop=0)

    
     