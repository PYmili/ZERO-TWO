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

kgmv = on_keyword({'/�ṷmv'}, to_me())

@kgmv.got('mv', prompt='���뿴ʲômv���ظ�mv����')
async def musice1(bot: Bot, state: T_State):
    mv = state['mv']
    if mv == '':
        await wyy.send("δ����ĸ���mv��")
    else:
        try:
            url = "https://api.iyk0.com/kgmv/?msg={}&n=1".format(mv)
            request = url
            re = requests.get(request)
            rep = re.json()
            mv = rep.get('mvtitle')
            zz = rep.get('singer')
            img = rep.get('img')
            mv_dz = rep.get('link')
            await kgmv.send(f"mv���ƣ�{mv}" + MessageSegment.image(img) + f"\n���ߣ�{zz}" + f"���ӣ�{mv_dz}")
        except:
            await kgmv.send("���ִ�������ϵPYmili��")
