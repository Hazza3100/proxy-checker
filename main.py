import queue
import threading

import requests


c = queue.Queue()
valid = []

with open('proxy.txt', 'r') as f:
    proxies = f.read().split('\n')
    for x in proxies:
        c.put(x)




def check():
    with requests.Session() as session:
        try:
            global c
            while not c.empty():
                proxy = c.get()
                r = session.get('https://ipinfo.io/ip', proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'})
                if r.status_code == 200:
                    print("valid proxy")
                    open('valid.txt', 'a').write(f'{proxy}\n')
                else:
                    pass

        except:
            pass




b = len(open('proxy.txt', 'r').readlines())
for _ in range(b):
    threading.Thread(target=check).start()
