import os
from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

milipython = on_keyword({'/MiliPython'})

@milipython.got('Python', prompt='回复代码运行')
async def Python_mili(bot: Bot, state: T_State):
    py = state['Python']
    if py == '':
        await milipython.send("没有代码了！变态！")
    elif py in 'while True':
        await milipython.send("不要用循环了！笨蛋！")
    else:
        with open(r'F:/PYTHON/python程序/qq机器人/ZERO-TWO/src/plugins/md/run.py', 'w+', encoding='utf-8-sig') as f:
            f.write(f"{py}")
        result = os.popen('python F:/PYTHON/python程序/qq机器人/ZERO-TWO/src/plugins/md/run.py 2>&1')
        context = result.read()
        await milipython.send(context)
        result.close()
and_print = on_keyword({'Mili>--print'})
@and_print.got('print', prompt='--print(Message=str, number=int, for_=for, while_=while)')
async def Python_print(bot: Bot, state: T_State):
    pr = state['print']
    if pr == '':
        await and_print.send("Pass!")
    else:
        await and_print.send(f"{pr}")
