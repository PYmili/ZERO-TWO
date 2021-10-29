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

bqb = on_keyword({'/�������ѯ'})

@bqb.got('bq', prompt='����Ҫ��ѯ�ı����.')
async def yq_(bot: Bot, state: T_State):
    bq = state['bq']
    if bq == '':
        await bqb.send("Ϊʶ��Ҫ��ѯ�ı������")
    else:
        try:
            url="https://api.iyk0.com/sbqb/?msg={}".format(bq)
            request=url
            re=requests.get(request)
            rep = re.json()

            code = rep.get('code')
            msg = rep.get('msg')
            keyword = rep.get('keyword')
            sums = rep.get('sum')
            data_img = rep.get('data_img')

            for i in data_img:
                img = i['img']
                await bqb.send(MessageSegment.image(f"{img}"))
        except:
            print("���ִ�������ϵPYmili�޸���")
