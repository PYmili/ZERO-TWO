import time
import datetime
import os

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
    
qd = on_keyword({'/签到'})

@qd.got('qd', prompt='1.查询签到记录， 2.创建用户, 3.签到，4.清空用户')
async def qd_r(bot: Bot, event: Event, state: T_State):
    q = state['qd']
    id = str(event.get_user_id()) # 获取用户QQ号用于创建.txt文件
    msg_time = datetime.datetime.now() # 获取系统时间用于签到
    if q == '查询签到记录' or q == '1':
        jl = os.path.exists(f'F:\\PYTHON\\python程序\\qq机器人\\ZERO-TWO\\src\\plugins\\md\\{id}.txt') # 检查文件是否存在
        if jl == True:
            with open(f'F:\\PYTHON\\python程序\\qq机器人\\ZERO-TWO\\src\\plugins\\md\\{id}.txt', 'r', encoding='utf-8') as f:
                read = f.read() # 读取文件所有内容
            await qd.send(f'{read}') # print
        else:
            await qd.send(f'没有找到你的签到文件，请创建用户吧！') # Eroor
    elif q == '创建用户' or q == '2':
        try:
            true_ues = os.path.exists(f'F:\\PYTHON\\python程序\\qq机器人\\ZERO-TWO\\src\\plugins\\md\\{id}.txt')
            if true_ues == True:
                await qd.send('笨蛋！你已经有用户了！你想脚踏两只船吗？')
            else:
                with open(f'F:\\PYTHON\\python程序\\qq机器人\\ZERO-TWO\\src\\plugins\\md\\{id}.txt', 'w+', encoding='utf-8') as n:
                    new = f"user{id} = ['{msg_time}创建记录!']"
                    n.write(new)
                await qd.send('创建成功！')
        except:
            await qd.send('创建失败！')
    elif q == '签到' or q == '3':
        try:
            with open(f'F:\\PYTHON\\python程序\\qq机器人\\ZERO-TWO\\src\\plugins\\md\\{id}.txt', 'a', encoding='utf-8') as a:
                a.write(f'\n{msg_time}：签到！')
                await qd.send(f'{msg_time}：签到！')
        except:
            await qd.send('Error!')
    elif q == '清空用户' or q == '4':
        try:
            yes_no = os.path.exists(f'F:\\PYTHON\\python程序\\qq机器人\\ZERO-TWO\\src\\plugins\\md\\{id}.txt')
            if yes_no == True:
                os.remove(f'F:\\PYTHON\\python程序\\qq机器人\\ZERO-TWO\\src\\plugins\\md\\{id}.txt')
                await qd.send('删除成功！')
            else:
                await qd.send('没有这个用户，笨蛋！')
        except:
            await qd.send('删除失败！Eroor')
    else:
        await qd.send('你是笨蛋吗？根本没有这个命令！')
