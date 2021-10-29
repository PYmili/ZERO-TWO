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

game = on_keyword({'/游戏查询', '/game'}, to_me())

@game.got('game', prompt='您想查询哪款游戏？')
async def musice1(bot: Bot, state: T_State):
    g = state['game']
    if g == '':
        await game.send('変態暇にしないでください!')
    else:
        url="https://api.iyk0.com/yyb/?msg={}&n=1".format(g)
        request=url
        re=requests.get(request)
        rep = re.json()
        code = rep.get('code')
        name = rep.get('name')
        js = rep.get('introduce')
        img = rep.get('icon')
        bb = rep.get('edition')
        size = rep.get('size')
        url_ = rep.get('downUrl')
        await game.send(MessageSegment.image(f"{img}"))
        await game.send(name)
        await game.send(js)
        await game.send(f"版本：{bb}")
        await game.send(f"大小：{size}")
        await game.send(f"下载链接：{url_}")
