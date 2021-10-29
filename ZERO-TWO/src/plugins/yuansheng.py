#coding:gbk
import requests
import json

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event
from nonebot.adapters.cqhttp.message import MessageSegment
from nonebot.permission import *
from nonebot.rule import to_me
import json

yuansheng = on_keyword({'/ԭ������'}, to_me())

@yuansheng.got('ys', prompt='��ѡ��ҳ��1-25')
async def ys_xw(bot: Bot, state: T_State):
    ys = state['ys']
    mlu = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
           '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
           '23', '24', '25']
    if ys in mlu:
        url = f"http://47.108.189.192/API/yuanshengxw/{ys}.json"
        rep = requests.get(url=url).json()
        bt = rep.get('����')
        fbsj = rep.get('����ʱ��')          
        nr = rep.get("����")
        img = rep.get('ͼƬ')
        fmmc = rep.get('�������Ƽ�����')
        img_list = []
        for im in img.split():
            img_list.append(im)
        num = 0
        if len(fmmc) == 0:
            nr_list = []
            for read in nr.split(' ��'):
                nr_list.append(f'{read}')
            await yuansheng.send(f"���⣺{bt}\n����ʱ�䣺{fbsj}")
            for re in nr_list:
                await yuansheng.send(f"{re}")
            for n in img_list:
                await yuansheng.send(MessageSegment.image(f"{img_list[num]}"))
                num += 1
        else:
            for f in fmmc:
                await yuansheng.send(MessageSegment.image(f"{f['url']}") + f"���⣺{bt}\n����ʱ�䣺{fbsj}\n\n���ݣ�{nr}")
                for n in img_list:
                    await yuansheng.send(MessageSegment.image(f"{img_list[num]}"))
                    num += 1
    else:
        await yuansheng.send('�㶢���ҿ�������������أ�')
