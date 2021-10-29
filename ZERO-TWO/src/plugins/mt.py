from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

'''美腿'''
mt = on_keyword({"美腿"}, to_me())
@mt.handle()
async def xiansm_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    await mt.send(MessageSegment.image('https://api.iyk0.com/mtt') + "精选美腿！少看点！")

'''精选美图'''
jxmt = on_keyword({"美图诱惑"}, to_me())
@jxmt.handle()
async def xiansx_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    await jxmt.send(MessageSegment.image('https://api.iyk0.com/mtyh') + "精选美图诱惑！少看点！")
