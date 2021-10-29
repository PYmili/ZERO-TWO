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

kgmv = on_keyword({'/酷狗mv'}, to_me())

@kgmv.got('mv', prompt='您想看什么mv？回复mv歌名')
async def musice1(bot: Bot, state: T_State):
    mv = state['mv']
    if mv == '':
        await wyy.send("未输入的歌名mv！")
    else:
        try:
            url = "https://api.iyk0.com/kgmv/?msg={}&n=1".format(mv)
            request = url
            re = requests.get(request)
            rep = re.json()
            mv = rep.get('mvtitle')
            zz = rep.get('singer')
            img = rep.get('img')
            mv_dz = rep.get('link')
            await kgmv.send(f"mv名称：{mv}" + MessageSegment.image(img) + f"\n作者：{zz}" + f"链接：{mv_dz}")
        except:
            await kgmv.send("发现错误！请联系PYmili！")
