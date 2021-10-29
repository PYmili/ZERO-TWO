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

sj_pz = on_keyword({'/手机配置查询'}, to_me())

@sj_pz.got('pz', prompt='请输入手机机型')
async def musice1(bot: Bot, state: T_State):
    p = state['pz']
    if p == '':
        await sj_pz.send("未输入的配置！")
    else:
        sj = p
        await sj_pz.send(f"您输入的机型是{sj}")
        await sj_pz.send("正在为您查询！")
        url="https://api.iyk0.com/sjzx/?msg={}".format(sj)
        request=url
        rep=requests.get(request) 
        repJson = rep.json()
        code = repJson.get('code')
        msg = repJson.get('msg')
        sums = repJson.get('sums')
        data = repJson.get('data')
        await sj_pz.send(f"{code}")
        await sj_pz.send(f"{msg}")
        for i in data:
            await sj_pz.send(f"手机品牌：{i['手机品牌']}")
            await sj_pz.send(f"机型图片：" + MessageSegment.image(f"{i['机型图片']}"))
            await sj_pz.send(f"上市时间：{i['上市时间']}")
            await sj_pz.send(f"描述价格：{i['描述价格']}")
            await sj_pz.send(f"手机配置：{i['手机配置']}")
