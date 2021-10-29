#coding:gbk

import requests
import datetime

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

ls = on_keyword({'/历史上的今天'}, to_me())

@ls.handle()
async def ls_r(bot: Bot, event: Event, state: T_State):
    try:
        res_ls = requests.get('https://api.iyk0.com/lishi/')

        json_ls = res_ls.json()

        yue = (datetime.datetime.now().month)
        if yue > 9:
            y = f"{yue}"
        else:
            y = f"0{yue}"
        re = (datetime.datetime.now().day)
        if re > 9:
            r = f"{re}"
        else:
            r = f"0{re}"
        ry = f"{y}月{r}日"
        list_ls = json_ls[ry]
        for i in list_ls:
            await ls.send(f"{i['year']}|{i['title']}\n")
    except:
        await ls.send("发现错误！请联系PYmili修复！")
