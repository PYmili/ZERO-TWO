from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

from urllib.request import urlopen
from bs4 import BeautifulSoup as Be
import urllib.parse
import string


xh = on_keyword({"笑话"}, to_me())
#cd=on_command('',rule=to_me(),priority=5)
@xh.handle()
async def xh_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    url = ("https://api.iyk0.com/xh/")
    urls = urllib.parse.quote(url, safe=string.printable)
    html = urlopen(f"{urls}")
    bs = Be(html, features="lxml")

    html_div = bs.findAll("body")
    mess = (html_div[0].get_text())
    await xh.send(MessageSegment.at(id) + f"{mess}")
