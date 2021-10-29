#coding:gbk
from urllib.request import urlopen
from bs4 import BeautifulSoup as Be
import urllib.parse
import string

from nonebot import on_command,on_keyword
from nonebot.adapters.cqhttp import Bot, Event
from nonebot.rule import to_me

lt = on_keyword("#", to_me())

@lt.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()
    if args:
        state["user_msg"] = args


@lt.got("user_msg", prompt="你想和我聊些什么？")
async def handle_user(bot: Bot, event: Event, state: dict):
    user_msg = state["user_msg"]
    user_msg_message = await get_lt(user_msg)
    #await lt.finish(user_msg_message)


async def get_lt(user_msg: str):
    message = user_msg.strip("#")
    url = ("https://api.iyk0.com/liaotian/?msg={}").format(message)
    urls = urllib.parse.quote(url,safe=string.printable)
    html = urlopen(f"{urls}")
    bs = Be(html,features="lxml")

    html_div = bs.findAll("body")
    mesage = (html_div[0].get_text())
    fst = await lt.send(f"{mesage}")
    return fst
