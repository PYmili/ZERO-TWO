#coding:gbk
from urllib.parse import urlencode
import requests
import urllib
import json

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me



baidu_rs = on_keyword({"/百度热搜"}, to_me())
#=on_command('夸我',rule=to_me(),priority=5)
@baidu_rs.handle()
async def baidu_r(bot: Bot, event: Event, state: T_State):
    url = "https://api.iyk0.com/bdr/"
    request = url
    # print(request)
    # 读取请求结果
    rep = requests.get(request)
    # 请求结果转换成json格式
    repJson = rep.json()
    code = repJson.get('code')
    msg = repJson.get('msg')
    data = repJson.get('data')
    dic = {'code': code, 'msg': msg, 'data': data}
    id = str(event.get_user_id())
    num = 0
    print("百度热搜榜\n")
    await baidu_rs.send(MessageSegment.at(id))
    for i in data:
        num += 1
        mes1 = i['title']
        mes2 = i['url']
        await baidu_rs.send(f"第{num}条热搜{mes1}" + f"\n{mes2}")
        #await baidu_rs.send(f"{mes2}")
