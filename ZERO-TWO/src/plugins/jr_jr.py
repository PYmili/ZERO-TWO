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



jrjr = on_keyword({"今日节日"}, to_me())
@jrjr.handle()
async def jrjr_r(bot: Bot, event: Event, state: T_State):
    url = "https://api.iyk0.com/jr/"
    request = url
    re = requests.get(request)
    rep = re.json()

    today = rep.get('today')
    surplus = rep.get('surplus')
    await jrjr.send(f"{today}")
    await jrjr.send(f"{surplus}")
    #await jrjr.send(f"{tips}")
