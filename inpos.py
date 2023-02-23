import random
import os
import requests
import time
from timeout_decorator import timeout, TimeoutError
hi = 'http://145.40.103.113:3128/'
os.environ['https_proxy'] = hi
print(hi)

ui = []


l = [
            'http://145.40.121.201:3128/',

            'http://117.5.76.119:4005/',

            'http://65.108.230.239:45569/',#

            'http://187.72.98.130:8080/',#

            'http://5.78.50.231:8888/',

            'http://134.195.157.37:3128/',

            'http://20.241.236.196:3128/',

            'http://133.186.215.90:3128/',

            'http://198.74.101.82:1994/',

            'http://173.82.12.238:1994/',

            'http://173.82.12.10:1994/',

            'http://169.0.113.180:8080/',

            'http://163.172.31.44:80/',

            'http://173.82.102.194:1994/',#

            'http://173.82.12.10:1994/',

            'http://213.136.94.25:3128/',

            'http://165.232.77.180:8080/',

            'http://165.232.75.40:8080/',

            'http://185.135.157.89:8080/',

            'http://102.165.51.172:3128/',

            'http://216.127.188.23:1994/',

            'http://155.94.220.8:1994/'         
            ]

ui = l






def gav():
    u = 0

    try:
        try:
            len(l)
            time.sleep(1)
            u = u + 1

            if  u == 1:
                
                rks = random.choice(l)
                os.environ['https_proxy'] = rks
                print(rks)
                r = requests.get("https://discordapp.com/", timeout=5)
                print(r.status_code)

                if r.status_code == 200:
                    print(u)
                    u = 0
                elif r.status_code == 429 :
                    print(u)
                    print("out")
                    u = 0
        except IndexError:
            l == ui
            gav()
    except:
        print("timeout")
        gav()

def jos():

    gav()

