import requests
from tkinter import *
from tkinter import messagebox
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController


import re
import json
import os
import time

headers = {
    'User-Agent': 'unknown',
    'X-ANNOTATOR-AUTH-TOKEN':'unknown'
	# 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
	# 'X-ANNOTATOR-AUTH-TOKEN':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcGVuX2lkIjoiYzI1YzJkNjJhYjBjNDE1MTgxZTRkZjY1NjljMGQyM2EiLCJuYW1lIjoiIiwiZW1haWwiOiIiLCJhZG1pbmlzdHJhdG9yIjpmYWxzZSwiZXhwIjoxNjE3MDkyODE4MjYyLCJpc3MiOiJjNGY3NzIwNjNkY2ZhOThlOWM1MCIsImF1ZCI6ImVkeC51bmlwdXMuY24ifQ.G8J9KaXuc5tNfaaZ8f-zBqcZ3bIQm2oGA16SoV_zrRw'
    # # #请从自己的浏览器中获取
}

keyboard_c  = KeyboardController()
timestamp_win = 0

r=Tk()
r.title("Uniqus killer")
r.geometry('300x140')

###-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-###
def update_agent():
    headers['User-Agent']=user_agent.get()
    headers['X-ANNOTATOR-AUTH-TOKEN']=x_token.get()

def fun_Info(event):
    messagebox.showinfo('Arter Infomation',\
                        "Autor:R0\nEmail:boogieling_o@qq.com\nCopyright © 2020 Ling rights reserved.")
###-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-###

def start_answer_1():
    update_agent()
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
    entry_1.delete(0,END)

def start_answer_2():
    update_agent()
    url_deal = url.get().split('/')
    target_url = 'https://ucontent.unipus.cn/course/api/content/'+url_deal[5]+'/'+url_deal[-2]+'/default/'
    answer_str=""
    try : 
        rec = requests.get(target_url,headers = headers).text
    except  requests.exceptions.ConnectionError:
        print('URL输入错误')
    pos = 1
    word_2 = re.findall(r"answers.*?:.*?\"(.*?)\".*?,",rec)
    if word_2 :
        for word in word_2:
            word_3 = "".join(re.findall(r"[A-Z0-9a-z -]",word))    
            
            print(str(pos)+'题答案：'+word_3)
            answer_str+=str(pos)+'题答案：'+word_3
            answer_str+="\n"
            pos = pos + 1
    else:
        word_2 = re.findall(r"answer.*?:.*?\"(.*?)\".*?,",rec)
        if word_2 :
            for word in word_2:
                word_3 = "".join(re.findall(r"[A-Z0-9a-z -]",word))    
                
                print(str(pos)+'题答案：'+word_3)
                answer_str+=str(pos)+'题答案：'+word_3
                answer_str+="\n"
                pos = pos + 1
        else:
            print('网址错误或其他问题，未能获取答案。\n')
            print("请检查网络，或稍后重试。\n")
            answer_str+="答案爬取失败\n请检查网络\n或是此题没有答案"
            time.sleep(2)
    messagebox.showinfo('答案',answer_str)
    entry_1.delete(0,END)
###-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-###
tmp_user_agent="''"
tmp_x_token="''"
if os.path.exists('config.r0')==True :
    f = open("config.r0","r")   #设置文件对象
    line = f.readline()
    line = line[:-1]
    r_pos= 0
    while line:             #直到读取完文件
        line = f.readline()  #读取一行文件，包括换行符
        print(line)
        line = line[:-1]     #去掉换行符，也可以不去
        if r_pos==0:
            tmp_user_agent=line
        elif r_pos==1:
            tmp_x_token=line
        r_pos+=1
        if line=="__END__" :
            break
    f.close() #关闭文件
else:
    with open("config.r0","w") as f :
        f.writelines("__BEGIN__\n")
        f.writelines("'Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'\n")
        f.writelines("'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcGVuX2lkIjoiYzI1YzJkNjJhYjBjNDE1MTgxZTRkZjY1NjljMGQyM2EiLCJuYW1lIjoiIiwiZW1haWwiOiIiLCJhZG1pbmlzdHJhdG9yIjpmYWxzZSwiZXhwIjoxNjE3MDkyODE4MjYyLCJpc3MiOiJjNGY3NzIwNjNkY2ZhOThlOWM1MCIsImF1ZCI6ImVkeC51bmlwdXMuY24ifQ.G8J9KaXuc5tNfaaZ8f-zBqcZ3bIQm2oGA16SoV_zrRw'\n")
        f.writelines("__END__")
        tmp_user_agent="'Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'"
        tmp_x_token="'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcGVuX2lkIjoiYzI1YzJkNjJhYjBjNDE1MTgxZTRkZjY1NjljMGQyM2EiLCJuYW1lIjoiIiwiZW1haWwiOiIiLCJhZG1pbmlzdHJhdG9yIjpmYWxzZSwiZXhwIjoxNjE3MDkyODE4MjYyLCJpc3MiOiJjNGY3NzIwNjNkY2ZhOThlOWM1MCIsImF1ZCI6ImVkeC51bmlwdXMuY24ifQ.G8J9KaXuc5tNfaaZ8f-zBqcZ3bIQm2oGA16SoV_zrRw'"
    f.close() #关闭文件


#url = input('请输入需要获取答案的URL:\n(大部分不计分的题目以及单元测试是没有答案的）')
#创建容器
f_1 = Frame(r)
f_1.place(x=10,y=0)
#标签1
l_1 = Label(f_1,text="user-agent")
l_1.pack()
#标签2
l_2 = Label(f_1,text="X-...-TOKEN")
l_2.pack()
#标签3
l_3 = Label(f_1,text="URL")
l_3.pack()

#创建容器
f_2 = Frame(r)
f_2.place(x=100,y=0)


user_agent = StringVar()
entry_2 = Entry(f_2,width=20,textvariable=user_agent)
entry_2.insert(0,tmp_user_agent)
entry_2.pack()

x_token = StringVar()
entry_3 = Entry(f_2,width=20,textvariable=x_token)
entry_3.insert(0,tmp_x_token)
entry_3.pack()

url = StringVar()
entry_1 = Entry(f_2,width=20,textvariable=url)
entry_1.pack()

#创建容器
f_3 = Frame(r)
f_3.place(x=50,y=90)

button_1=Button(f_3, 
                text="I AM LAZY",
                command=start_answer_1)#响应botton
button_1.pack()

#创建容器
f_4 = Frame(r)
f_4.place(x=150,y=90)

button_2=Button(f_4, 
                text="JUST ANSWER",
                command=start_answer_2)#响应botton
button_2.pack()

r.wm_attributes('-topmost',1) #置顶
r.bind("<Tab>",fun_Info)#响应按键
r.resizable(0,0)

r.mainloop()

