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
import linecache
import datetime


matcher = on_keyword({'打开命令行'}, to_me())


a = 0

@matcher.got('chat', prompt='您有什么指示？')
async def chat1(bot: Bot, state: T_State):
    chat = state['chat']
    if chat == '关闭' or chat == 'q':
        await matcher.finish("再见！")
    elif chat == '时间':
        now_time = await time()
        await matcher.send("现在已经{now_time}点啦!")
    elif chat == '信息轰炸>>':
        for i in range(10):
            await matcher.send("信息轰炸！")
    else:
        message = chat
        url = ("https://api.iyk0.com/liaotian/?msg={}").format(message)
        urls = urllib.parse.quote(url,safe=string.printable)
        html = urlopen(f"{urls}")
        bs = Be(html,features="lxml")
        html_div = bs.findAll("body")
        mesage = (html_div[0].get_text())
        await matcher.send(f"{mesage}")
async def time():
    return datetime.datetime.now().strftime('%I %T').split()[0]

