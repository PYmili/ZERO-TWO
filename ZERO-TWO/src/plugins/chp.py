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


caihongpi = on_keyword({"����"}, to_me())
#caihongpi=on_command('����',rule=to_me(),priority=5)
@caihongpi.handle()
async def xiansm_r(bot: Bot, event: Event, state: T_State):
    url = "https://api.iyk0.com/chp/"
    request = url
    re = requests.get(request)
    rep = re.json()
    txt = rep.get('txt')
    id = str(event.get_user_id())
    await caihongpi.send(MessageSegment.at(id) + f"{txt}")
