from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me
"""cos"""
matcher = on_keyword({"cos"}, to_me())
#matcher=on_command('cos',rule=to_me(),priority=5)
@matcher.handle()
async def xian_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:image,file=https://api.iyk0.com/cos,cache=0]"
    #await matcher.send(Message(cq))
    #await matcher.send(MessageSegment.at(id) + xians)
    await matcher.send(MessageSegment.image('https://api.iyk0.com/cos') + "少看点")
