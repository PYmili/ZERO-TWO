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

yq = on_keyword({'/�������'}, to_me())

@yq.got('yq', prompt='������в�ѯ�������(һ�ν�֧��һ�˲�ѯ��������ִ������Ե�һ����)��')
async def yq_(bot: Bot, state: T_State):
    yq_cs = state['yq']
    if yq_cs == '':
        await yq.send("δʶ�𵽳��У�")
    else:
        try:
            url="https://api.iyk0.com/yq/?msg={}".format(yq_cs)
            request=url
            re=requests.get(request)
            rep = re.json()

            cxdq = rep.get('��ѯ����')
            mqqz = rep.get('Ŀǰȷ��')
            swrs = rep.get('��������')
            zyrs = rep.get('��������')
            xzqz = rep.get('����ȷ��')
            xcqz = rep.get('�ִ�ȷ��')
            xcwzz = rep.get('�ִ���֢״')
            time = rep.get('time')
            await yq.send(f"����ѯ�ĳ����ǣ�{cxdq}\nĿǰȷ������Ϊ��{mqqz}\n��������Ϊ��{swrs}\n��������Ϊ��{zyrs}\n����ȷ������Ϊ��{xzqz}\n�ִ�ȷ������Ϊ��{xcqz}\n�ִ���֢״Ϊ��{xcwzz}\nʱ�䣺{time}\n\nZERO-TWU����������ϴ�֣���ϴ�裬���˶����������")
        except:
            print("���ִ�������ϵPYmili�޸���")
