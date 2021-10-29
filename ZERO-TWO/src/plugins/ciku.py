from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from nonebot.rule import to_me

'''主人'''
pymili = on_keyword({"主人","你的主人是谁？","你的主人是谁","创造者","pymili","PYmili"}, to_me())
#matcher=on_command('主人',rule=to_me(),priority=5)
@pymili.handle()
async def pymili_r(bot: Bot, event: Event, state: T_State):
    img = "https://codechina.csdn.net/qq_53280175/image_py/-/raw/master/2f15ee0623de8f6b.jpg"
    #await pymili.send("test")
    await pymili.send(MessageSegment.image(f'{img}') + '我主人是PYmili')



'''我们的官网'''
matcher=on_keyword({"我们的官网","我们的官网是多少？","官网"}, to_me())
@matcher.handle()
async def _(bot: Bot, event: Event, state: T_State):
    guabw = "https://47.108.189.192/" #"www.pydome.icu" 
    await matcher.send('我们的官网是' + guabw)

'''哭表情'''
ku=on_keyword({'哭','快哭','你给我哭'}, to_me())

@ku.handle()
async def ku_r(bot: Bot, event: Event, state: T_State):
    biaoqing = f"[CQ:face,id=5]"  # 表情包使用
    await ku.send(Message(biaoqing) + 'ZERO-TWO：不会哭的！')

'''戳'''
cuo = on_keyword({'戳','戳一戳'}, to_me())

@cuo.handle()
async def cuo_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    # mes = str()
    chuo = f"[CQ:poke,qq={id}]"
    await cuo.send(Message(chuo))

'''你是谁'''
you = on_keyword({'你叫什么名字','你是谁','你是谁呀','你是','你到底是谁'}, to_me())

@you.handle()
async def you_(bot: Bot, event: Event, state: T_State):
    await you.send('我是ZERO-TWO，一个聪明的孩子，可以对我说 菜单')


'''在吗'''
matchemr = on_keyword({'在吗', '你好', 'hi'}, to_me())

@matchemr.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await matchemr.send('我在，有什么事吗？ 可以对我说 菜单')

'''age'''
age = on_keyword({"你多大了","age","你现在多大了","你几岁了","你现在几岁了"}, to_me())
@age.handle()
async def age_(bot: Bot, event: Event, state: T_State):
    await age.send('我现在才1岁呢！')

'''hello'''
hello = on_keyword({"你好","你好？","你好呀"}, to_me())
@hello.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await hello.send("你好呀！我是ZREO-TWO！ 可以对我说 菜单")

'''男，女'''
mesx = on_keyword({"男生还是女生","女生","男生","男孩子","女孩子","男性","女性"}, to_me())
@mesx.handle()
async def mesx_(bot: Bot, event: Event, state: T_State):
    await mesx.send("我是女生哦！")


"""
'''骂人'''
ma = on_keyword({'妈的','操','草','你妈','傻逼','智障','人工智障','傻','垃圾','辣鸡'})
@ma.handle()
async def ma_r(bot: Bot, event: Event, state: T_State):
    await ma.send(MessageSegment.image("http://img.doutula.com/production/uploads/image/2019/11/17/20191117989079_bqlnus.jpg") + "骂人是不好的呀！不要骂人呀！")
"""
'''开心'''
kaix = on_keyword({"开心","快乐","心情好"}, to_me())
@kaix.handle()
async def m_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    biaoqings = f"[CQ:face,id=28]"
    await kaix.send(Message(biaoqings) + "笑着过一生！")

'''ZERO-TWO'''
ZERO = on_keyword({"ZERO-TWO"})
@ZERO.handle()
async def p_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    ZE = f"[CQ:face,id=21]"
    await kaix.send(Message(ZE) + "ZERO-TWO:我在！你要对我说什么？")


'''晚安'''
wan = on_keyword({"晚安"}, to_me())
@wan.handle()
async def wan_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    wan = f"[CQ:face,id=75]"
    await kaix.send(Message(wan) + "晚安！做个好梦呀！")

'''晚上好'''
wnans = on_keyword({"晚上好"}, to_me())
@wnans.handle()
async def wanns_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    wan = f"[CQ:face,id=180]"
    await wnans.send(Message(wan) + "晚上好呀，要早点睡觉哦！")
    #await wnans.send(MessageSegment(f'{tp}'))


'''早上好'''
zao = on_keyword({"早上好","早安","早！"}, to_me())
@zao.handle()
async def zao_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    zao = f"[CQ:face,id=21]"
    await kaix.send(Message(zao) + "早安！今天又是美好的一天！")

'''中午好'''
zowu = on_keyword({"中午好","午安","午！"}, to_me())
@zowu.handle()
async def zowu_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    zowu = f"[CQ:face,id=74]"
    await kaix.send(MessageSegment.at(id) + zowu + "午安！下午也要精神满满呀！")


"""编写代码的现实！"""
xians = on_keyword({"招聘程序员"}, to_me())
@xians.handle()
async def xians_r(bot: Bot, event: Event, state: T_State):
    #id = str(event.get_user_id())
    await xians.send(MessageSegment.image("https://codechina.csdn.net/qq_53280175/image_py/-/raw/master/2aab7b4f0bc587c3.jpg") + "这就是现实！")


'''-----从入门到放弃------'''
rm = on_keyword({"从入门到放弃","还没入门就放弃"}, to_me())
@rm.handle()
async def rm_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    #xians = f"[CQ:image,file=http://47.108.189.192/wp-content/uploads/2021/07/6abfd2e45462fa83-300x300.jpg,cache=0]"
    await rm.send(MessageSegment.image('https://codechina.csdn.net/qq_53280175/image_py/-/raw/master/6abfd2e45462fa83-300x300.jpg') + "少年你渴望力量吗？")

'''----------网络爬虫师----------'''
wlpc = on_keyword({"网络爬虫"}, to_me())
@wlpc.handle()
async def wlpc_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    #xians = f"[CQ:image,file=http://47.108.189.192/wp-content/uploads/2021/07/6abfd2e45462fa83-300x300.jpg,cache=0]"
    await wlpc.send(MessageSegment.image('https://codechina.csdn.net/qq_53280175/image_py/-/raw/master/-1bc1c0b3b3101e20.jpg') + "孩子，爬虫需谨慎")



'''---------回复-----------'''
hfu = on_keyword({"你怎么知道你聪明","智商","知道聪明"}, to_me())
@hfu.handle()
async def hfu_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    #xians = f"[CQ:image,file=https://api.iyk0.com/mn/2,cache=0]"
    url="https://api.iyk0.com/sbqb/?msg=可爱"
    request=url
    re=requests.get(request)
    rep = re.json()
    data_img = rep.get('data_img')
    img = data_img[0]['img']
    await hfu.send(MessageSegment.image(f'{img}') + "我可是很聪明的！智商..... 智商可以吃吗？")


'''---------------随机美图---------------'''
mtu = on_keyword({"随机美图","美图"}, to_me())
@mtu.handle()
async def mtu_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    #xians = f"[CQ:image,file=https://api.iyk0.com/mn/2,cache=0]"
    await mtu.send(MessageSegment.image('https://api.iyk0.com/mn/2') + "美图都是随机生成的哦！")

'''---------------------LSP------------------------'''
LSPs = on_keyword({"LSP","我是LSP","lsp","我是LSP"}, to_me())
@LSPs.handle()
async def SLP_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    zp = f"[CQ:image,file=https://thumbnail0.baidupcs.com/thumbnail/5aa78152eqedb9b4854e476901e91dd8?fid=1103052109416-250528-722734976993320&time=1627743600&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-8gCA6xiHo%2F87DDhrXqFOl4IN6QY%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=304557084170085043&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video,cache=0,id=40000]"
    xians = f"[CQ:face,id=179]"
    await LSPs.send(MessageSegment.at(id) + "没想到你是LSP！你可以对我说：随机美图，cos,美图诱惑，美腿，美女图片，手机美女，随机二次元图片")

'''-------------------------随机美女图片----------------------------------'''
mntp = on_keyword({"随机美女图片","美女图片","美女"}, to_me())
@mntp.handle()
async def mntp_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    #xians = f"[CQ:image,file=https://api.iyk0.com/sjmn,cache=0]"
    await mntp.send(MessageSegment.image('https://api.iyk0.com/sjmn') + "美女图片都是随机生成的哦！")


'''------------------------------我是谁---------------------------------'''
wss = on_keyword({"我是谁","我是"}, to_me())
@wss.handle()
async def wss_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    xians = f"[CQ:face,id=183]"
    await wss.send("你是" + MessageSegment.at(id) + Message(xians) + "真可爱！")


'''-------------------------随机二次元图片----------------------------------'''
ecy_tp = on_keyword({"随机二次元图片","二次元图片","二次元"}, to_me())
#mntp=on_command('随机二次元图片',rule=to_me(),priority=5)
@ecy_tp.handle()
async def ecy_tp_r(bot: Bot, event: Event, state: T_State):
    id = str(event.get_user_id())
    #xians = f"[CQ:image,file=https://api.iyk0.com/ecy/api.php,cache=0]"
    await ecy_tp.send(MessageSegment.image('https://api.iyk0.com/ecy/api.php') + "图片都是随机生成的哦！")


bxxx = on_keyword({"不想学习","学习有什么用","不学习"}, to_me())
@bxxx.handle()
async def bxxx_r(bot: Bot, event: Event, state: T_State):
    #id = str(event.get_user_id())
    url="https://api.iyk0.com/sbqb/?msg=不想学习"
    request=url
    re=requests.get(request)
    rep = re.json()
    data_img = rep.get('data_img')
    await bxxx.send("不学习等于没技术，没技术等于没工作，没工作等于没生活。没生活等于废材！")
    await bxxx.send(MessageSegment.image(f"{data_img[0]['img']}"))

