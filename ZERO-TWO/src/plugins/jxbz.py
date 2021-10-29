from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

'''精选壁纸'''
#xians = on_keyword({""})
matcher=on_keyword('精选壁纸', to_me())
@matcher.handle()
async def xians_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    bz = f"https://api.iyk0.com/jxbz"
    await matcher.send(MessageSegment.image(bz) + "精选壁纸！")
