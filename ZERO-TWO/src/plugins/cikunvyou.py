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
import linecache
import datetime


matcher = on_keyword({'��������'}, to_me())


a = 0

@matcher.got('chat', prompt='����ʲôָʾ��')
async def chat1(bot: Bot, state: T_State):
    chat = state['chat']
    if chat == '�ر�' or chat == 'q':
        await matcher.finish("�ټ���")
    elif chat == 'ʱ��':
        now_time = await time()
        await matcher.send("�����Ѿ�{now_time}����!")
    elif chat == '��Ϣ��ը>>':
        for i in range(10):
            await matcher.send("��Ϣ��ը��")
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

