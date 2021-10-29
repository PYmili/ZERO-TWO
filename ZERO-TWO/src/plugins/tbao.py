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

tbao = on_keyword({'/搜索淘宝商品'}, to_me())

@tbao.got('sp', prompt='请输入要搜索的物品')
async def taobao(bot: Bot, state: T_State):
    sp = state['sp']
    biantai = ['避孕套', '肉便器', '充气娃娃', '飞机杯', '跳蛋']
    if sp == '':
        await tbao.send("ばか、何を言っていますか！")
    elif sp in biantai:
        await tbao.send("変態！死ね!")
    elif sp == 'ZERO-TWO':
        await tbao.send("あなたのこの大変態!")
    else:
        url = (f"https://api.iyk0.com/tbsp/?msg={sp}")
        urls = urllib.parse.quote(url,safe=string.printable)
        html = urlopen(f"{urls}")
        bs = Be(html,features="lxml")

        html_div = bs.findAll("body")
        await tbao.send(f"{html_div[0].get_text()}")
