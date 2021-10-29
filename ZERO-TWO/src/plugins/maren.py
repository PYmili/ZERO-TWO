#coding:gbk
import requests

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me


maren = on_keyword({"骂我"}, to_me())
#caihongpi=on_command('夸我',rule=to_me(),priority=5)
@maren.handle()
async def maren_r(bot: Bot, event: Event, state: T_State):
    url = "http://47.108.189.192/API/maren"
    re = requests.get(url=url)
    txt = str(re.text)
    id = str(event.get_user_id())
    await maren.send(MessageSegment.at(id) + f"{txt}")
