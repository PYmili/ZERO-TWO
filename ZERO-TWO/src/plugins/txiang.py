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

tx = on_keyword({'/ͷ��ͼƬ'}, to_me())

@tx.got('tx', prompt='��������Ҫ��ͷ�����ͣ�Ů���У����������£�')
async def tx1(bot: Bot, state: T_State):
    x = state['tx']
    cmd = ['Ů', '��', '����']
    if x == '����':
        url="https://api.iyk0.com/sjtx/?msg={}".format(x)
        request=url
        re=requests.get(request)
        rep = re.json()
    
        code = rep.get('code')
        img1 = rep.get('img1')
        img2 = rep.get('img2')
        await tx.send(MessageSegment.image(f"{img1}"))
        await tx.send(MessageSegment.image(f"{img2}"))
    elif x in cmd:
        url="https://api.iyk0.com/sjtx/?msg={}".format(x)
        request=url
        re=requests.get(request)
        rep = re.json()
    
        code = rep.get('code')
        img = rep.get('img')
        await tx.send(MessageSegment.image(f"{img}"))
    else:
        await tx.send("��B�֤���ޤ���")
