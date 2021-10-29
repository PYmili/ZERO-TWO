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

dm = on_keyword({'/������ѯ'}, to_me())

@dm.got('tx_dm', prompt='��ظ��������֣�')
async def musice1(bot: Bot, state: T_State):
    tx = state['tx_dm']
    if tx == '':
        await dm.send("������Ϊ�գ�")
    else:
        url="https://api.iyk0.com/txmh/?msg={}&n=1".format(tx)
        request=url
        re=requests.get(request)
        rep = re.json()
        
        code = rep.get('code')
        title = rep.get('title')
        img = rep.get('img')
        author = rep.get('author')
        time = rep.get('time')
        type_ = rep.get('type')
        js = rep.get('introduce')
        url_ = rep.get('url')
        if code == 201:
            await dm.send("û���ҵ����������")
        else:
            await dm.send(f'��������{title}')
            await dm.send(f'Image��' + MessageSegment.image(f'{img}'))
            await dm.send(f'���ߣ�{author}')
            await dm.send(f'����ʱ�䣺{time}')
            await dm.send(f'���ͣ�{type_}')
            await dm.send(f'���ܣ�{js}')
            await dm.send(f'��ַ��{url_}')
