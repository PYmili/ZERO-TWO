#coding:utf-8
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

QQ_JZ = on_keyword({'/QQ报价', '/qq报价'})

@QQ_JZ.got('QQ', prompt='输入要查询的QQ，回复价格(一次仅支持一人查询，如果发现错请您稍等一下下)')
async def QQ_JZ_(bot: Bot, state: T_State):
    qq = state['QQ']
    if qq == '':
        await QQ_JZ.send("未识别到城市！")
    else:
        try:
            url="https://api.iyk0.com/qqgj/?qq={}".format(qq)
            request=url
            re=requests.get(request)
            rep = re.json()
            code = rep.get('code')
            qqmm = rep.get('QQ号码')
            qqws = rep.get('QQ位数')
            qqjz = rep.get('QQ价值')
            gxsj = rep.get('更新时间')
            yqts = rep.get('友情提示')
            await QQ_JZ.send('QQ号码：' + qqmm)
            await QQ_JZ.send('QQ位数：' + qqws)
            await QQ_JZ.send('QQ价值：' + qqjz)
            await QQ_JZ.send('更新时间：' + gxsj)
            await QQ_JZ.send('友情提示：' + yqts)
        except:
            await QQ_JZ.send("发现错误！请联系PYmili修复！")
