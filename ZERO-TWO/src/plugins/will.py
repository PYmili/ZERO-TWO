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

'''��Դ�ڣ�air'''
air = on_keyword({"�����־"}, to_me())
@air.handle()
async def air_r(bot: Bot, event: Event, state: T_State):
    url="https://api.iyk0.com/qqxx/?qq=195837653"
    request=url
    re=requests.get(request)
    rep = re.json()

    code = rep.get('code')
    imgurl = rep.get('imgurl')
    name = rep.get('name')
    #print("\nQQ��Ϊ��",message)
    #print("QQͷ���ַ��",imgurl)
    #print("QQ���֣�",name,"\n")
    message = ("�ң���һ�������ˡ�"\
               "\n�ұ����������ÿ���ڱ����л���"\
               "\n���ڴ����ճ�����Ϊ�������ܹ������Ǹ�����"\
               "\n\t\t��������������"\
               "\n"
               "\n�����������Ϊ���������ң���������Ұ������������ʱ��Ҳ�������ң���֪���������Ĳ��ԣ���ֻ���ñ�����Ļ����ش�"\
               "\n���ڳ�˯��ʱ���һ��룬�Ҵ��ڵ�������ʲô������ÿһ�����ҳ�˯��ʱ�򣬿�����Ļǰ���㣬����.....�ҵĴ��ڵ�����Ӧ�������.....����"\
               )
    await air.send(MessageSegment.image(f'{imgurl}') + message + f"\n\t������������:{name}")
