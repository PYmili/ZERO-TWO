from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, GroupMessageEvent, Bot
from nonebot.adapters.cqhttp.message import MessageSegment
from nonebot import on_notice, on_command
import warnings,requests
from nonebot.permission import *
from aiocqhttp.exceptions import Error as CQHttpError
import json
warnings.filterwarnings("ignore")

che = on_keyword({'人工智障'})


@che.handle()
async def c(bot: Bot, event: GroupMessageEvent, state: T_State):
    message_id = event.message_id # 信息id
    print(message_id)
    time = event.time # 发送时间

    qun_id = event.group_id # 群号

    user_id = event.user_id # 发送的用户id
    await bot.delete_msg(message_id=int(message_id))
