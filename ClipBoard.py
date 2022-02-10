import pyperclip
import time
import re


email = input('email, на который произойдет замена: ')
print('для выхода -> Ctrl + C. \nскрипт в процессе...')


old = ''
try:
    while True:
        s = pyperclip.paste()
        if s != old:
            pyperclip.copy(re.sub(r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$', email, s))
            old = s
        time.sleep(1)
except KeyboardInterrupt:
    print('готово.')

