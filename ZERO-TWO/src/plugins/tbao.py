#coding:gbk
from urllib.request import urlopen
from bs4 import BeautifulSoup as Be
import urllib.parse
import string


from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 宸曾倖短喘議艶評
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

tbao = on_keyword({'/朴沫猛右斌瞳'}, to_me())

@tbao.got('sp', prompt='萩補秘勣朴沫議麗瞳')
async def taobao(bot: Bot, state: T_State):
    sp = state['sp']
    biantai = ['閲墅耗', '扉宴匂', '割賑抑抑', '敬字鵜', '柳軌']
    if sp == '':
        await tbao.send("ばか、採を冱っていますか��")
    elif sp in biantai:
        await tbao.send("���B�）世�!")
    elif sp == 'ZERO-TWO':
        await tbao.send("あなたのこの寄���B!")
    else:
        url = (f"https://api.iyk0.com/tbsp/?msg={sp}")
        urls = urllib.parse.quote(url,safe=string.printable)
        html = urlopen(f"{urls}")
        bs = Be(html,features="lxml")

        html_div = bs.findAll("body")
        await tbao.send(f"{html_div[0].get_text()}")
