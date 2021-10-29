from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

'''-------------听歌表情-----------'''

tg = on_keyword({"喜欢听歌吗","听歌吗"}, to_me())
#tg=on_command('',rule=to_me(),priority=5)
@tg.handle()
async def bxxx_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    await tg.send(MessageSegment.at(id) + "我很喜欢听歌的！")

'''-------------无聊表情-----------------'''
wl = on_keyword({"无聊"}, to_me())
@wl.handle()
async def wl_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())    
    await wl.send(MessageSegment.at(id) + "ZERO-TWO也很无聊！")

'''-----------------疲倦表情---------------------'''
pj = on_keyword({"疲倦","累不累"}, to_me())
@pj.handle()
async def pj_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())    
    await wl.send(MessageSegment.at(id) + "很累！")
