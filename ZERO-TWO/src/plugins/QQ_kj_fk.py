#coding:gbk
from urllib.parse import urlencode
import requests
import urllib
import json

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # ������û�õı�ɾ
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

fw = on_keyword({'/QQ�ռ��������ѯ'}, to_me())

@fw.got('fwl', prompt='�ظ����ѯ��QQ')
async def musice1(bot: Bot, state: T_State):
    f = state['fwl']
    if f == '':
        await fw.send("�����̬��QQ������д��")
    elif f == '241757256':
        await fw.send("���ʤ��Ή�B��")
    else:
        url="https://api.iyk0.com/qzone/?qq={}".format(f)
        request=url
        re=requests.get(request)
        rep = re.json()
        code = rep.get('code')
        msg = rep.get('msg')
        data = rep.get('data')
        if code == 201:
            await fw.send("���ؤ󤿤�!û���ҵ�����˵�QQ��")
        else:
            await fw.send(msg)
            await fw.send(data)
