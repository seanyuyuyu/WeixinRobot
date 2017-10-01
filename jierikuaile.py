#!python3
import itchat
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling
from tuling import get_response
from itchat.content import *

@itchat.msg_register('Text')
def text_reply(msg):
    if '你是谁' in msg['Text'] or '主人' in msg['Text']:
        return '我是余晓光的机器人，聊聊吧'
    elif '国庆' in msg['Text'] or '快乐' in msg['Text']:
        itchat.send('国庆节快乐！', msg['FromUserName'])
    elif '获取图片' in msg['Text']:
        itchat.send('@img@applaud.gif', msg['FromUserName']) # there should be a picture
    else:
        return get_response(msg['Text']) or '收到：' + msg['Text']

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({ 'Picture': '图片', 'Recording': '录音',
        'Attachment': '附件', 'Video': '视频', }.get(msg['Type']) +
        '已下载到本地') # download function is: msg['Text'](msg['FileName'])

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return '收到位置分享'
    elif msg['Type'] == 'Sharing':
        return '收到分享' + msg['Text']
    elif msg['Type'] == 'Note':
        return '收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return '收到好友信息：' + msg['Text']['Alias']

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if '国庆' in msg['Text'] or '快乐' in msg['Text']:
        return '国庆节快乐'#get_response(msg['Text']) or '收到：' + msg['Text']

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('我是余晓光的机器人\n'
        + '他很忙，经常在开会\n' + '图片获取：回复获取图片\n'
        + '所以有什么事先来找我吧！', msg['RecommendInfo']['UserName'])

itchat.auto_login(enableCmdQR=-2)
itchat.run()
