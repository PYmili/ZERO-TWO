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

dsp = on_keyword({'/ˢ��Ƶ'}, to_me())

@dsp.got('sp', prompt='���뿴ʲô������Ƶ�����죬���ǣ����裬�羰����Ϸ�����')
async def musice1(bot: Bot, state: T_State):
    sp = state['sp']
    string = ['����', '����', '����', '�羰', '��Ϸ', '����']
    if sp in string:
        url="https://api.iyk0.com/dsp/?type={}".format(sp)
        request=url
        re=requests.get(request)
        rep = re.json()
        code = rep.get('code')
        img = rep.get('img')
        type_ = rep.get('type')
        url_ = rep.get('url')
        # video = f"[CQ:video,file={url_}]"
        await dsp.send(f"���棺" + MessageSegment.image(f"{img}"))
        await dsp.send(f"���⣺{type_}")
        await dsp.send(f"��Ƶ" + url_)
    else:
        await dsp.send(f"û��{sp}������������ǲ���ɵ��")
