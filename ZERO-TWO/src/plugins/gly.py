#coding:gbk

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # ������û�õı�ɾ
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
    
gly = on_keyword({'/����Ա'}, to_me())

@gly.got('glyuan', prompt='����֤������ݣ�')
async def Python_(bot: Bot, state: T_State):
    gl = state['glyuan']
    glylist = []
    with open(r'F:\PYTHON\python����\qq������\ZERO-TWO\src\plugins\md\gly.txt', 'r+', encoding='utf-8') as li:
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
        await gly.send(f"����Ա{gl}��ã�")
    else:
        await gly.send("Ϊ���ִ˹���Ա������")
        
