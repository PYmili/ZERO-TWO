from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

cd = on_keyword({"菜单", "/help", "/HELP", "/Help"}, to_me())
#cd=on_command('菜单',rule=to_me(),priority=1)
@cd.handle()
async def cd_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    cd_list = ("\1.菜单查看所有功能名称\n"\
               "\n2.我是lsp\n"\
               "\n3.早上好，晚上好，中午好，晚安，早安\n"\
               "\n4.你的主人是谁？,官网,你叫什么名字，在吗\n"\
               "\n5.笑，哭，戳,多大了，你好，男生，开心，ZERO-TWO，招聘程序员\n"\
               "\n6.从入门到放弃，我是谁，不想学习,几点了，几年，喜欢听歌吗？\n"\
               "\n7.无聊，累不累，个人博客，ZERO-TWO的家，天气，钢铁侠\n"\
               "\n8.夸我，/百度热搜，毒鸡汤，今日节日，笑话"\
               "\n9./酷狗mv，#和机器人聊天，/点歌，/QQ报价，/历史上的今天，/疫情情况，/表情包查询，你的意志\n"\
               "\n10.土味情话，舔狗日记，/刷视频，/手机配置查询，/漫画查询，/QQ空间访问量查询，/game\n"\
               '\n11./搜索淘宝商品，/翻译，/MiliPython，/签到\n'
               "\n除了私聊不需要@群聊需要@")
    await cd.send(MessageSegment.at(id) + f"{cd_list}")
