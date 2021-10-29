#coding:gbk
from urllib.request import urlopen
from bs4 import BeautifulSoup as Be
import urllib.parse
import string


from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # ������û�õı�ɾ
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

tbao = on_keyword({'/�����Ա���Ʒ'}, to_me())

@tbao.got('sp', prompt='������Ҫ��������Ʒ')
async def taobao(bot: Bot, state: T_State):
    sp = state['sp']
    biantai = ['������', '�����', '��������', '�ɻ���', '����']
    if sp == '':
        await tbao.send("�Ф����Τ��ԤäƤ��ޤ�����")
    elif sp in biantai:
        await tbao.send("��B������!")
    elif sp == 'ZERO-TWO':
        await tbao.send("���ʤ��Τ��δ��B!")
    else:
        url = (f"https://api.iyk0.com/tbsp/?msg={sp}")
        urls = urllib.parse.quote(url,safe=string.printable)
        html = urlopen(f"{urls}")
        bs = Be(html,features="lxml")

        html_div = bs.findAll("body")
        await tbao.send(f"{html_div[0].get_text()}")
