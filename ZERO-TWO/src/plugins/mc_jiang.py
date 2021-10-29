from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

"""cos"""
#xians = on_keyword({"cos"})
mc=on_command('随机mc酱壁纸', to_me())
@mc.handle()
async def mc_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    mcs = f"https://api.iyk0.com/mc/mcapi.php"
    await matcher.send(MessageSegment.image(mcs) + "mc酱壁纸都是随机的哦！")
