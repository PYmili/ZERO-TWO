from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, GroupMessageEvent, GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent, \
    GroupUploadNoticeEvent, GroupAdminNoticeEvent, GroupRecallNoticeEvent, PokeNotifyEvent,Bot
from nonebot.adapters.cqhttp.message import MessageSegment
from nonebot import on_notice, on_command
import warnings,requests
from nonebot.permission import *
from aiocqhttp.exceptions import Error as CQHttpError
import json
warnings.filterwarnings("ignore")
# 检测离开群成员
group_decrease = on_notice()


@group_decrease.handle()
async def handle_first_receive(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
    rely = [
        {
            "type": "text",
            "data": {
                "text": "这位小可爱"
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
                "text": "退群咯啦！"
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
                "text": "一路走好，小心脚滑！"
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

