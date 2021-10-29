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

dsp = on_keyword({'/刷视频'}, to_me())

@dsp.got('sp', prompt='您想看什么类型视频（网红，明星，热舞，风景，游戏，动物）')
async def musice1(bot: Bot, state: T_State):
    sp = state['sp']
    string = ['网红', '明星', '热舞', '风景', '游戏', '动物']
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
        await dsp.send(f"封面：" + MessageSegment.image(f"{img}"))
        await dsp.send(f"标题：{type_}")
        await dsp.send(f"视频" + url_)
    else:
        await dsp.send(f"没有{sp}这个参数，你是不是傻？")
