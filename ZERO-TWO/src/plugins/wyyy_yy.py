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

wyy = on_keyword({'/���'}, to_me())

@wyy.got('musice', prompt='������ʲô�裿�ظ�����')
async def musice1(bot: Bot, state: T_State):
    mu = state['musice']
    if mu == '':
        await wyy.send("δ����ĸ�����")
    else:
        try:
            url="https://api.iyk0.com/wymusic/?msg={}&n=1".format(mu)
            request=url
            re=requests.get(request)
            rep = re.json()

            image = rep.get('img')
            img = image
            name = rep.get('song')
            zz = rep.get('singer')
            url_ = rep.get('url')
            yy = f"[CQ:music,type=custom,url={url_},audio={url_},content={name}����{zz},image={img}]"
            await wyy.send(Message(yy))
            # await wyy.send(MessageSegment.image(img) + f"\n������{name}\n���ߣ�{zz}\n" + url_)
        except:
            await wyy.send("���ִ�������ϵPYmili��")
