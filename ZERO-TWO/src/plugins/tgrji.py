#coding:gbk
from urllib.request import urlopen
from bs4 import BeautifulSoup as Be
import urllib.parse
import string

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

tgrj = on_keyword({"舔狗日记"}, to_me())
#=on_command('菜单',rule=to_me(),priority=1)
@tgrj.handle()
async def tgrj_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    url = ("https://api.iyk0.com/tiangou/")
    urls = urllib.parse.quote(url,safe=string.printable)
    html = urlopen(f"{urls}")
    bs = Be(html,features="lxml")

    html_div = bs.findAll("body")
    tg = (html_div[0].get_text())
    await tgrj.send(MessageSegment.at(id) + tg)
