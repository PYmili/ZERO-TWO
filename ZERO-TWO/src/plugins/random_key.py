#coding:gbk

import random


from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
    
key = on_keyword({'/生成随机秘钥'}, to_me())

@key.got('key', prompt='请输入位数')
async def Python_(bot: Bot, state: T_State):
    kk = state['key']
    if kk == '':
        await key.send("请输入参数！")
    else:
        key_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w',
                    'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f',
                    'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        ksy_list = []
        for i in range(int(kk)):
            klist = random.choice(key_list)
            ksy_list.append(klist)
        keys = "".join(ksy_list)
        await key.send(f"{keys}")
