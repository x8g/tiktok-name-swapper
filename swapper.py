#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import system
import os
import time 
from colorama import Fore, Back, Style
import sys
import json
import random
import warnings
import threading
import urllib3
from urllib.parse import urlencode
import threading
from threading import Thread
import ctypes


http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False) #disabled ssl cert verification
#default_headers = make_headers(proxy_basic_auth='myusername:mypassword') if wanna use proxy(you most likely will need and use some rotating proxy to bypass rate limit
#http = ProxyManager("https://myproxy.com:8080/", headers=default_headers)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')#disabled warnings
attempts=0
banner = 'zt\n'
system("title " + "zt#7380 Tiktok Swapper")
os.system('cls||clear')
print(Back.BLACK + Fore.BLUE + banner)
print('')
user = input(Back.BLACK + Fore.WHITE + " Enter @")
os.system('cls||clear')
print(Back.BLACK + Fore.BLUE + banner)
print(Fore.CYAN + '          Session ID')
print('')
print('')
sid = input(Fore.BLUE+" root" + Fore.WHITE+"@" + Fore.MAGENTA +"zt" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+" ")
os.system('cls||clear')
print(Back.BLACK + Fore.BLUE
      + banner)
print(Fore.CYAN + '          Threads')
print('')
print('')
threads = int(input(Fore.BLUE+" root" + Fore.WHITE+"@" + Fore.MAGENTA +"zt" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+" "))
ctypes.windll.user32.MessageBoxW(0, "Starting...", "Swapper", 0)
os.system('cls||clear')






def swapper():  
    global attempts    
    system("title " + f"Attempts ~ {attempts}")
    url='https://api16-normal-c-useast1a.tiktokv.com/passport/login_name/update/?iid=7114694905583191810&device_id=7103265913999754757&ac=wifi&channel=googleplay&aid=1180&app_name=trill&version_code=240302&version_name=24.3.2&device_platform=android&ab_version=24.3.2&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=es&os_api=25&os_version=7.1.2&openudid=6d1bc771d91a26d2&manifest_version_code=240302&resolution=720*1280&dpi=239&update_version_code=240302&_rticket=1656719123822&current_region=NL&app_type=normal&sys_region=ES&mcc_mnc=20420&timezone_name=Europe%2FMadrid&residence=NL&ts=1656719121&timezone_offset=3600&build_number=24.3.2&region=ES&uoo=0&app_language=es&carrier_region=NL&locale=es&op_region=NL&ac2=wifi&host_abi=x86_64&cdid=fc486ba0-9c73-4837-93ef-023891876356&support_webview=1&okhttp_version=4.1.73.30-tiktok'#TIKTOK API ENDPOINT
    data = {'login_name': user} 
    encoded_data = urlencode(data)
    res = http.request(
        'POST',
        url,
        body=encoded_data,
        headers={ # get the headers by using memu + http toolkit and changing top name
        "accept-encoding": "gzip",
        "connection": "Keep-Alive",
        "content-length": "66",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": f"sessionid={sid}",
        "host": "api16-normal-useast5.us.tiktokv.com",
        "multi_login": "1",
        "passport-sdk-version": "19", 
        "sdk-version": "2",
        "user-agent": "com.zhiliaoapp.musically/2022402040 (Linux; U; Android 7.1.2; en; G011A; Build/N2G48H;tt-ok/3.10.0.2)",
        "x-argus": "j0vsJZR2PZD4yoBSNCrLfX+OGBqG0MkHQTBdGmqcLd1JPegrnK4MzcTTBzQWBiGJePTVx1bpsxDLRw2OBDTcbZl/fhlPo8FJEmOtLG/aGQj61OFIKrkVPjn7xs9a31qurC6A3EfGXZDMuSwAgRN7wUwGuMkVLtMgjj7mc7mdA6fpZd4vKpXupP2Tqq6RLgtw2J8wp4yxKxPxuavLCe1NWVQsAeZdxNuGJ71lFqdZo+D4jUUt2+YudUCZYNoe0yLkN5nEJGSgLEfnHmGZdbsUJM8uUKKJfHlDBMnP+Ro8vpq76g==",
        "x-gorgon": "040480cd0000586c8f7662e8d4b10fffdefc0460e2d824bfd43d",
        "x-khronos": "1657653393",
        "x-ladon": "8/JuLbZJi+p9B6umkaS7VZMRuhWsMkCQvSG3oL1OfTiOLz83",
        "x-ss-req-ticket": "1657653393627",
        "x-ss-stub": "188EA5AA4CB76B59CE892769CB64C232",
        "x-tt-cmpl-token": "AgQQAPPdF-RPsLJnYRP69Z0XwU_4xwJfv4fZYMYI0A",
        "x-tt-dm-status": "login=1;ct=1;rt=1",
        "x-tt-multi-sids": "7086853493826733102%3Abac83f0539f006fdeaa98765249e3eef",
        "x-tt-store-region": "us",
        "x-tt-store-region-src": "uid",
        "x-tt-token": "04bac83f0539f006fdeaa98765249e3eef007a9046ce06cc5e21837a8f9b5a0ee12099e67117cda4ab3f19443a7ef235e7c100c39545cb3d64f9db81b1655cefdb692f7c0140dee42bbbdd35543ae944211d1fb7662ef28019f9223f01a79aa57958f-1.0.1",
        "x-vc-bdturing-sdk-version": "2.2." 
        })
    attempts+=1
    #print(res.data.decode('utf-8'))
    if '"message":"success"' in res.data.decode('utf-8'): 
        print(Back.BLACK + Fore.GREEN + f'\nSuccessfully swapped @{user.strip()}'+ Back.BLACK + Fore.WHITE)
        print('\n\t by zt')
        sys.exit()
    elif 'login name can only be updated once within one month.' in res.data.decode('utf-8'):
        print(Back.BLACK + Fore.YELLOW + f'\nNot Possible to change username(delay)' + Back.BLACK + Fore.WHITE)
        sys.exit()
    elif 'Only letters, numbers, underscores, or periods are allowed' in res.data.decode('utf-8'):
        sys.exit()
    #elif '"description":"This username is taken, but you can try a different one"' in res.data.decode('utf-8'):
    
    #elif '"description":"Too many attempts. Try again later."' in res.data.decode('utf-8'):
    
if type(threads) == int: #smart print
    print(Fore.WHITE + '[' + Fore.BLUE + '+' + Fore.WHITE + ']' + f'Target ~ {Fore.MAGENTA}@{user}')
    print(Fore.WHITE + '[' + Fore.BLUE + '+' + Fore.WHITE + ']' + f'SessionID ~ {Fore.MAGENTA}{sid}')
    print(Fore.WHITE + '[' + Fore.BLUE + '+' + Fore.WHITE + ']' + f'Threads ~ {Fore.MAGENTA} {threads}')
     
    
    
tag=True

while tag == True: #just an animation
    print(Fore.WHITE + '\r[' + Fore.BLUE + '\\' + Fore.WHITE + ']' + Fore.MAGENTA + 'zt' + Fore.WHITE, end='')
    time.sleep(0.1)
    print(Fore.WHITE + '\r[' + Fore.BLUE + '/' + Fore.WHITE + ']' + Fore.MAGENTA + 'zt' + Fore.WHITE, end='')
    for i in range(threads):
        [].append(threading.Thread(target=swapper).start())
    for threadz in []:
        threadz.join()
