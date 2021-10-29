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

fw = on_keyword({'/QQ空间访问量查询'}, to_me())

@fw.got('fwl', prompt='回复想查询的QQ')
async def musice1(bot: Bot, state: T_State):
    f = state['fwl']
    if f == '':
        await fw.send("你个变态！QQ都不会写！")
    elif f == '241757256':
        await fw.send("あなたの変態！")
    else:
        url="https://api.iyk0.com/qzone/?qq={}".format(f)
        request=url
        re=requests.get(request)
        rep = re.json()
        code = rep.get('code')
        msg = rep.get('msg')
        data = rep.get('data')
        if code == 201:
            await fw.send("死へんたい!没有找到这个人的QQ！")
        else:
            await fw.send(msg)
            await fw.send(data)
