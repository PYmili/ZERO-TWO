#coding:gbk
from urllib.parse import urlencode
import requests
import urllib
import json

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

wyy = on_keyword({'/点歌'}, to_me())

@wyy.got('musice', prompt='您想听什么歌？回复歌名')
async def musice1(bot: Bot, state: T_State):
    mu = state['musice']
    if mu == '':
        await wyy.send("未输入的歌名！")
    else:
        try:
            url="https://api.iyk0.com/wymusic/?msg={}&n=1".format(mu)
            request=url
            re=requests.get(request)
            rep = re.json()

            image = rep.get('img')
            img = image
            name = rep.get('song')
            zz = rep.get('singer')
            url_ = rep.get('url')
            yy = f"[CQ:music,type=custom,url={url_},audio={url_},content={name}作者{zz},image={img}]"
            await wyy.send(Message(yy))
            # await wyy.send(MessageSegment.image(img) + f"\n歌名：{name}\n作者：{zz}\n" + url_)
        except:
            await wyy.send("发现错误！请联系PYmili！")
