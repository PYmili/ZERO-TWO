#coding:gbk
from urllib.parse import urlencode
import requests
import urllib
import json

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

dm = on_keyword({'/漫画查询'}, to_me())

@dm.got('tx_dm', prompt='请回复漫画名字！')
async def musice1(bot: Bot, state: T_State):
    tx = state['tx_dm']
    if tx == '':
        await dm.send("您输入为空！")
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
            await dm.send("没有找到这个漫画！")
        else:
            await dm.send(f'动漫名：{title}')
            await dm.send(f'Image：' + MessageSegment.image(f'{img}'))
            await dm.send(f'作者：{author}')
            await dm.send(f'更新时间：{time}')
            await dm.send(f'类型：{type_}')
            await dm.send(f'介绍：{js}')
            await dm.send(f'地址：{url_}')
