#coding:gbk

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
    
gly = on_keyword({'/管理员'}, to_me())

@gly.got('glyuan', prompt='请验证您的身份！')
async def Python_(bot: Bot, state: T_State):
    gl = state['glyuan']
    glylist = []
    with open(r'F:\PYTHON\python程序\qq机器人\ZERO-TWO\src\plugins\md\gly.txt', 'r+', encoding='utf-8') as li:
        read = li.readlines()
        num = 0
        for i in range(len(read)):
            reads = ''.join(read[num])
            num += 1
            glylist.append(reads.replace('\n', ''))
        li.close()
    print(glylist)
    if gl == '':
        await gly.send("Error !")
    elif gl in glylist:
        await gly.send(f"管理员{gl}你好！")
    else:
        await gly.send("为发现此管理员！滚！")
        
