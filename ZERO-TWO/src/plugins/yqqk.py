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

yq = on_keyword({'/疫情情况'}, to_me())

@yq.got('yq', prompt='输入城市查询疫情情况(一次仅支持一人查询，如果发现错请您稍等一下下)。')
async def yq_(bot: Bot, state: T_State):
    yq_cs = state['yq']
    if yq_cs == '':
        await yq.send("未识别到城市！")
    else:
        try:
            url="https://api.iyk0.com/yq/?msg={}".format(yq_cs)
            request=url
            re=requests.get(request)
            rep = re.json()

            cxdq = rep.get('查询地区')
            mqqz = rep.get('目前确诊')
            swrs = rep.get('死亡人数')
            zyrs = rep.get('治愈人数')
            xzqz = rep.get('新增确诊')
            xcqz = rep.get('现存确诊')
            xcwzz = rep.get('现存无症状')
            time = rep.get('time')
            await yq.send(f"您查询的城市是：{cxdq}\n目前确诊人数为：{mqqz}\n死亡人数为：{swrs}\n治愈人数为：{zyrs}\n新增确诊人数为：{xzqz}\n现存确诊人数为：{xcqz}\n现存无症状为：{xcwzz}\n时间：{time}\n\nZERO-TWU提醒您：勤洗手，勤洗澡，多运动，少外出！")
        except:
            print("发现错误！请联系PYmili修复！")
