from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

gtx = on_keyword({"Iron Man","Iron_Man","iron man","iron_man","钢铁侠"}, to_me())
#cd=on_command('',rule=to_me(),priority=5)
@gtx.handle()
async def bxxx_r(bot: Bot, event: Event, state: T_State):
    xians = ("\n\nIron Man"\
    		"\n“Failure is the fog through which we glimpse triumph”"\
			"\n“失败是迷雾，穿过它，我们就可以瞥见光明。”"\
			"\n\n\t——钢铁侠 《复仇者联盟3》")
    my = ("\n\n\nYou can take away my house"\
			"\n你可以夺走我的房子"\
			"\nAll my tricks and toys"\
			"\n也可以拿走我的小把戏小玩具"\
			"\nOne thing you can’t take away..."\
			"\n但你夺不走的是"\
			"\nI am Iron Man"\
			"\n我就是钢铁侠"\
			"\n\n——钢铁侠 《钢铁侠3》")
    id = str(event.get_user_id())
    await gtx.send(MessageSegment.at(id))
    await gtx.send(MessageSegment.image("http://image11.m1905.cn/uploadfile/2013/0327/20130327104108527.jpg") + xians + MessageSegment.image("https://codechina.csdn.net/qq_53280175/image_py/-/raw/master/v2-fca6b92268bfe2ab3be1a5914fa16378_r.jpg") + my)
