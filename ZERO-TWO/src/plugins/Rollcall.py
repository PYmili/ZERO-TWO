import random

from nonebot import require
import nonebot
import time
import requests

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

import json
import requests

dm = on_keyword({"点名"})
@dm.handle()
async def dm_r(bot: Bot, event: Event, state: T_State):
    url='https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
    headers={'Host':'qun.qq.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Accept-Encoding':'gzip, deflate, br',
            'Referer':'https://qun.qq.com/member.html',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With':'XMLHttpRequest',
            'Content-Length':'45',
            'Origin':'https://qun.qq.com',
            'Cookie':'pgv_pvid=9173611605; RK=K+oRNJF7RX; ptcz=f97efd3fe5babbd56a70201c93540f0e38177e0b8add3f7f0634e249bd406bdc; tvfe_boss_uuid=7e01ab435a97c69c; pac_uid=0_7cbd05b903643; iip=0; eas_sid=j1j6r3e131T6N4u6689995l2y7; ptui_loginuin=2097632843; _qpsvr_localtk=0.8099455361591548; uin=o2097632843; p_uin=o2097632843; traceid=18fc3d4a6f; skey=@EwOkxoaHe; pt4_token=EVXyY*wWQI3pETTz5n5bcDIuPM516AnL4WeBG*vYL8s_; p_skey=sPl2jiuUuRuRaL*Zeqb6UtiirBhoIoFYFMSgU76n*dI_',
            'Connection':'keep-alive',
             'TE':'Trailers'}
    data={'gc':"706128290",
        'st':"0",
        'end':"20",
       'sort':"0",
        'bkn':"872500496"}

    datas={'gc':"706128290",
        'st':"21",
        'end':"30",
       'sort':"0",
        'bkn':"872500496"}
    req=requests.post(url,headers=headers,data=data)
    req1=requests.post(url,headers=headers,data=datas)
    html=req.json()["mems"]
    html2=req1.json()['mems']
    qqnum_list=[]
    for i in html:
        json_file=dict(qqnum=i['uin'])
        qqnum_list.append(json_file['qqnum'])
    for j in html2:
        json_file=dict(qqnums=j['uin'])
        qqnum_list.append(json_file['qqnums'])
    print(qqnum_list)
    
    id = random.choice(qqnum_list)
    tu = "起来回答问题"
    await dm.send(MessageSegment.at(f'{id}') + tu)

dm_qt = on_keyword({"全体点名"})
@dm_qt.handle()
async def dm_r_qt(bot: Bot, event: Event, state: T_State):
    tu = "起来回答问题"
    at = f'[CQ:at,qq=all]'
    await dm_qt.send(Message(at))
    #for i in qqnum_list:
    #    await dm_qt.send(MessageSegment.at(f'{i}') + tu)
        
