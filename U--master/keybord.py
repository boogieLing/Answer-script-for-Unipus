from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time 

keyboard_c  = KeyboardController()
timestamp_win = 0

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
#while True:             #监控键盘
with keyboard.Listener( 
        on_press = on_press,
        on_release = on_release) as listener:
    listener.join()

