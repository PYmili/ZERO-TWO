#coding:gbk
from urllib.parse import urlencode
import requests
import urllib
import json

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # ������û�õı�ɾ
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me



djt = on_keyword({"������"}, to_me())
#=on_command('����',rule=to_me(),priority=5)
@djt.handle()
async def djt_r(bot: Bot, event: Event, state: T_State):
    url = "https://api.iyk0.com/du/"
    request = url
    re = requests.get(request)
    rep = re.json()

    name = rep.get('name')
    avatar = rep.get('avatar')
    data = rep.get('data')
    await djt.send(f"{name}")
    await djt.send(f"ͼƬ���ӣ�{avatar}")
    await djt.send(f"{data}")
