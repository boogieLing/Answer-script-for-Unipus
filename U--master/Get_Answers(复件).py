import requests
import pyperclip
from tkinter import Tk
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

import re
import json
import os
import time
#os.system("title U校园答案获取器")
os.system('echo -e "--U校园biss----\n----Made by r0----"')
#os.system("color 0a")
headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
	'X-ANNOTATOR-AUTH-TOKEN':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcGVuX2lkIjoiYzI1YzJkNjJhYjBjNDE1MTgxZTRkZjY1NjljMGQyM2EiLCJuYW1lIjoiIiwiZW1haWwiOiIiLCJhZG1pbmlzdHJhdG9yIjpmYWxzZSwiZXhwIjoxNjE3MDkyODE4MjYyLCJpc3MiOiJjNGY3NzIwNjNkY2ZhOThlOWM1MCIsImF1ZCI6ImVkeC51bmlwdXMuY24ifQ.G8J9KaXuc5tNfaaZ8f-zBqcZ3bIQm2oGA16SoV_zrRw'
    #请从自己的浏览器中获取
}
keyboard_c  = KeyboardController()
timestamp_win = 0

r=Tk()
r.withdraw()

def on_press(key):
    global timestamp_win #这里先引入一个全局变量,用于储存时间戳.
    try:  
        if key == Key.ctrl:     #判断按键为Windows键
            timestamp_win = time.time()   #如果是就把当前的时间存进去
        if key.char == '1':    #判断另一个按键
            if time.time() - timestamp_win <0.5: #如果2次按键的时间小于0.5s,就执行你想要执行的函数,比如我想执行search函数.
                print("right")
                keyboard_c.type("qwq")
    except AttributeError:      
        pass
 
def on_release(key): 
    #print('{0} released'.format(key)) 
    if key == keyboard.Key.esc: 
        return False

while(1):
    r.clipboard_clear()
    url = input('请输入需要获取答案的URL:\n(大部分不计分的题目以及单元测试是没有答案的）')
    url_deal = url.split('/')
    target_url = 'https://ucontent.unipus.cn/course/api/content/'+url_deal[5]+'/'+url_deal[-2]+'/default/'
    try : 
        rec = requests.get(target_url,headers = headers).text
        
    except  requests.exceptions.ConnectionError:
        print('URL输入错误')
    pos = 1
    word_2 = re.findall(r"answers.*?:.*?\"(.*?)\".*?,",rec)
    if word_2 :
        for word in word_2:
            word_3 = "".join(re.findall(r"[A-Z0-9a-z -]",word))    
            check_pos = word_3
            #r.clipboard_append(word_3)
            ##os.system("echo word_3 > /dev/clipboard")
            #pyperclip.copy(word_3)
            print(str(pos)+'题答案'+word_3)
            pos = pos + 1
    else:
        word_2 = re.findall(r"answer.*?:.*?\"(.*?)\".*?,",rec)
        if word_2 :
            for word in word_2:
                word_3 = "".join(re.findall(r"[A-Z0-9a-z -]",word))    
                check_pos = word_3
                #r.clipboard_append(word_3)
                ##os.system("echo word_3 > /dev/clipboard")
                #pyperclip.copy(word_3)
                print(str(pos)+'题答案'+word_3)
                pos = pos + 1
        else:
            #os.system("color 04")
            print('网址错误或其他问题，未能获取答案。\n')
            print("请检查网络，或稍后重试。\n")
            time.sleep(2)
            os.system("color 0a")
