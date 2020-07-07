import requests
from tkinter import *
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController


import re
import json
import os
import time


#os.system("title U校园答案获取器")
os.system('echo -e "--U校园biss----\n----Made by r0----"')
#os.system("color 0a")
headers = {
    # 'User-Agent': 'unknown',
    # 'X-ANNOTATOR-AUTH-TOKEN':'unknown'
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
	'X-ANNOTATOR-AUTH-TOKEN':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcGVuX2lkIjoiYzI1YzJkNjJhYjBjNDE1MTgxZTRkZjY1NjljMGQyM2EiLCJuYW1lIjoiIiwiZW1haWwiOiIiLCJhZG1pbmlzdHJhdG9yIjpmYWxzZSwiZXhwIjoxNjE3MDkyODE4MjYyLCJpc3MiOiJjNGY3NzIwNjNkY2ZhOThlOWM1MCIsImF1ZCI6ImVkeC51bmlwdXMuY24ifQ.G8J9KaXuc5tNfaaZ8f-zBqcZ3bIQm2oGA16SoV_zrRw'
    # #请从自己的浏览器中获取
}

keyboard_c  = KeyboardController()
timestamp_win = 0

r=Tk()
r.title("kill uniqus")

###-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-###
def start_answer_1():
    url_deal = url.get().split('/')
    target_url = 'https://ucontent.unipus.cn/course/api/content/'+url_deal[5]+'/'+url_deal[-2]+'/default/'
    try : 
        rec = requests.get(target_url,headers = headers).text
    except  requests.exceptions.ConnectionError:
        print('URL输入错误')
    pos = 1
    word_2 = re.findall(r"answers.*?:.*?\"(.*?)\".*?,",rec)
    time.sleep(5)
    if word_2 :
        for word in word_2:
            word_3 = "".join(re.findall(r"[A-Z0-9a-z -]",word))    
            check_pos = word_3
            keyboard_c.type( word_3 )
            #time.sleep(0.1)
            keyboard_c.press( Key.tab )
            keyboard_c.release( Key.tab )
            
            print(str(pos)+'题答案'+word_3)
            pos = pos + 1
    else:
        word_2 = re.findall(r"answer.*?:.*?\"(.*?)\".*?,",rec)
        if word_2 :
            for word in word_2:
                word_3 = "".join(re.findall(r"[A-Z0-9a-z -]",word))    
                check_pos = word_3
                keyboard_c.type( word_3 )
                #time.sleep(0.1)
                keyboard_c.press( Key.tab )
                keyboard_c.release( Key.tab )
                
                print(str(pos)+'题答案'+word_3)
                pos = pos + 1
        else:
            print('网址错误或其他问题，未能获取答案。\n')
            print("请检查网络，或稍后重试。\n")
            time.sleep(2)
    entry.delete(0,END)

def start_answer_2():
    url_deal = url.get().split('/')
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
            
            print(str(pos)+'题答案'+word_3)
            pos = pos + 1
    else:
        word_2 = re.findall(r"answer.*?:.*?\"(.*?)\".*?,",rec)
        if word_2 :
            for word in word_2:
                word_3 = "".join(re.findall(r"[A-Z0-9a-z -]",word))    
                check_pos = word_3
                
                print(str(pos)+'题答案'+word_3)
                pos = pos + 1
        else:
            print('网址错误或其他问题，未能获取答案。\n')
            print("请检查网络，或稍后重试。\n")
            time.sleep(2)
    entry.delete(0,END)
###-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-###


#url = input('请输入需要获取答案的URL:\n(大部分不计分的题目以及单元测试是没有答案的）')
url = StringVar()
entry = Entry(r,textvariable=url)
entry.pack()
button_1=Button(r, 
                text="I AM LAZY",
                command=start_answer_1)#响应botton
button_1.pack()
button_2=Button(r, 
                text="JUST ANSWER",
                command=start_answer_2)#响应botton
button_2.pack()
r.mainloop()




