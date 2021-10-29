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

tx = on_keyword({'/头像图片'}, to_me())

@tx.got('tx', prompt='请输入你要的头像类型（女，男，动漫，情侣）')
async def tx1(bot: Bot, state: T_State):
    x = state['tx']
    cmd = ['女', '男', '动漫']
    if x == '情侣':
        url="https://api.iyk0.com/sjtx/?msg={}".format(x)
        request=url
        re=requests.get(request)
        rep = re.json()
    
        code = rep.get('code')
        img1 = rep.get('img1')
        img2 = rep.get('img2')
        await tx.send(MessageSegment.image(f"{img1}"))
        await tx.send(MessageSegment.image(f"{img2}"))
    elif x in cmd:
        url="https://api.iyk0.com/sjtx/?msg={}".format(x)
        request=url
        re=requests.get(request)
        rep = re.json()
    
        code = rep.get('code')
        img = rep.get('img')
        await tx.send(MessageSegment.image(f"{img}"))
    else:
        await tx.send("変態分かりません！")
