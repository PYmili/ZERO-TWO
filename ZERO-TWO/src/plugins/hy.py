from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, GroupMessageEvent, GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent, \
    GroupUploadNoticeEvent, GroupAdminNoticeEvent, GroupRecallNoticeEvent, PokeNotifyEvent,Bot
from nonebot.adapters.cqhttp.message import MessageSegment
from nonebot import on_notice, on_command
import warnings,requests
from nonebot.permission import *

GroupIncrease = on_notice()

# 检测群成员增加
@GroupIncrease.handle()
async def handle_first_receive(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    rely = [
        {
            "type": "text",
            "data": {
                "text": "欢迎"
            }
        },
        {
            "type": "at",
            "data": {
                "qq": f"{event.user_id}"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "进群"
            }
        },
        {
            "type": "image",
            "data": {
                "file": f"https://q4.qlogo.cn/headimg_dl?dst_uin={event.user_id}&spec=640"
            }
        },
        {
            "type": "text",
            "data": {
                "text": "欢迎新人！大家努力学习呀！"
            }
        },
        {
            "type": "face",
            "data": {
                "id": "13"
            }
        }
    ]
    await bot.send(event=event, message=rely)
