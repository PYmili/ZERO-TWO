#coding:gbk
from urllib.parse import urlencode
import requests
import urllib
import json

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

fy = on_keyword({'/翻译'}, to_me())

@fy.got('fyq', prompt='输入中文翻译成英语。')
async def yq_(bot: Bot, state: T_State):
    yf_yw = state['fyq']
    if yf_yw == '':
        await fy.send("未识别到中文！")
    else:
        url="https://api.vvhan.com/api/fy?text={}".format(yf_yw)
        request=url
        re=requests.get(request)
        rep = re.json()

        data = rep.get('data')
        yw = data['fanyi']
        await fy.send(f"{yw}")
