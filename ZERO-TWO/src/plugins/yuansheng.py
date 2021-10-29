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

yuansheng = on_keyword({'/原神新闻'}, to_me())

@yuansheng.got('ys', prompt='请选择页数1-25')
async def ys_xw(bot: Bot, state: T_State):
    ys = state['ys']
    mlu = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
           '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
           '23', '24', '25']
    if ys in mlu:
        url = f"http://47.108.189.192/API/yuanshengxw/{ys}.json"
        rep = requests.get(url=url).json()
        bt = rep.get('标题')
        fbsj = rep.get('发布时间')          
        nr = rep.get("内容")
        img = rep.get('图片')
        fmmc = rep.get('封面名称及链接')
        img_list = []
        for im in img.split():
            img_list.append(im)
        num = 0
        if len(fmmc) == 0:
            nr_list = []
            for read in nr.split(' ▍'):
                nr_list.append(f'{read}')
            await yuansheng.send(f"标题：{bt}\n发布时间：{fbsj}")
            for re in nr_list:
                await yuansheng.send(f"{re}")
            for n in img_list:
                await yuansheng.send(MessageSegment.image(f"{img_list[num]}"))
                num += 1
        else:
            for f in fmmc:
                await yuansheng.send(MessageSegment.image(f"{f['url']}") + f"标题：{bt}\n发布时间：{fbsj}\n\n内容：{nr}")
                for n in img_list:
                    await yuansheng.send(MessageSegment.image(f"{img_list[num]}"))
                    num += 1
    else:
        await yuansheng.send('你盯着我看干嘛！你这个萝莉控！')
