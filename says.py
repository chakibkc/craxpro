import httpx as h
from bs4 import BeautifulSoup as bs
import random
from time import sleep
import json
from datetime import datetime
import pandas as pd 

def getxftoken():
    xf = input("give me the xftoken\n")
    return xf

def getcookies():
    cookies = {
    "craxcookie": "verified-apsvw7xhta4",
    "validated_bot": "9 27919 18 29",
    "validation_time": "Mon Sep 15 2025 22:07:49 GMT+0100 (Central European Standard Time)",
    "xf_csrf": "Xu-yVR6ovkgYwyod",
    "xf_sam_ad_views": "%7B%2252%22%3A1758040382%2C%2265%22%3A1758040425%2C%2263%22%3A1758040670%7D",
    "xf_session": "DshM3zVVhZ31BcOTzL-4FF5A3lme5f34",
    "xf_user": "14029%2ChBJrU08Kskx3_pnq03_vy-q_0Lqth4okOoDcRjk_",
}
    return cookies


def datagrap():
    with open("datacrax.txt","r") as r:
        lines = r.readlines()
        if(len(lines)==0):
            raise SystemError("Data Completed")
        if not lines:
            raise SystemError("the file is empty check the file again\n")
        st_line = lines[0].strip()
    with open("datacrax.txt" , "w") as r:
        r.writelines(lines[1:])
    return st_line

def titlegrap():
    with open("titlecrax.txt","r") as r:
        lines = r.readlines()
        if(len(lines)==0):
            raise SystemError("Data Completed")
        if not lines:
            raise SystemError("the file is empty check the file again\n")
        st_text = lines[0].strip()
    with open("titlecrax.txt" , "w") as r:
        r.writelines(lines[1:])
    return st_text

def check_len():
    with open("datacrax.txt", "r", encoding="utf-8") as f:
        l_data = sum(1 for _ in f)
    with open("titlecrax.txt", "r", encoding="utf-8") as r:
        l_title = sum(1 for _ in r)
    if (l_data != l_title):
        raise SystemError("the two files are not equal\n")

def count_success():
    print("")

tokens = [
    "bin",
    "cc card",    # 2. Linux - Firefox
    "2025",
    "shopify bin",
    "fresh",
    "cc",
    "shop",
    "bin shopify",
    "update",
    "cards",
]




headers_list = [

    # 1. Windows 10 - Chrome
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/134.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    },
    {
        "User-Agent": (
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) "
            "Gecko/20100101 Firefox/131.0"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    },

    # 3. macOS - Safari
    {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/17.5 Safari/605.1.15"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    },

    # 4. Android - Chrome Mobile
    {
        "User-Agent": (
            "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/134.0.0.0 Mobile Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    },

    # 5. iPhone - Safari
    {
        "User-Agent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/17.5 Mobile/15E148 Safari/604.1"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    },

    # 6. iPad - Safari
    {
        "User-Agent": (
            "Mozilla/5.0 (iPad; CPU OS 17_5 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/17.5 Mobile/15E148 Safari/604.1"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    },

    # 7. Windows 11 - Edge
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    },

    # 8. Linux - Chromium
    {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chromium/134.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    },

    # 9. macOS - Chrome
    {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/134.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    },

    # 10. Android - Firefox Mobile
    {
        "User-Agent": (
            "Mozilla/5.0 (Android 14; Mobile; rv:131.0) "
            "Gecko/20100101 Firefox/131.0"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    },
]
cookies = getcookies()
xf = getxftoken()

while(1):
    check_len()
    form_data = {
    "_xfToken": xf,
    "prefix_id[]": "130",
    "prefix_id_internal": "",
    "title": titlegrap(),
    "discussion_type": "discussion",
    "message_html": f"""
        <p style="text-align: center;">
            <span style="color: rgb(65, 168, 95);">
                <span style="font-size: 26px;"><strong>Link:</strong></span>
            </span>
        </p>
        <p style="text-align: center;">[REPLY]</p>
        <p style="text-align: center;"> Statue : ✅ {datagrap()} From @anti_public_cc_checker</p>
        <p style="text-align: center;">[/REPLY]</p>
    """,
    "attachment_hash": "4ec41f3ad6719c00a8f5780c3578d8f4",
    "attachment_hash_combined": '{"type":"post","context":{"node_id":73},"hash":"4ec41f3ad6719c00a8f5780c3578d8f4"}',
    "tokens_select": tokens,
    "tags": ", ".join(tokens),
    "watch_thread": "1",
    "_xfSet[watch_thread]": "1",
    "meta_title": "",
    "meta_description": "",
    "meta_ogimage": "",
    "nodeId": "73",
    "_xfRequestUri": "/forums/freebie.73/post-thread",
    "_xfWithData": "1",
    "_xfResponseType": "json",
}

    select = random.randint(0,8)
    header = headers_list[select]

    with h.Client(follow_redirects=True , timeout=15.0) as Client:
        r = Client.post("https://craxpro.io/forums/freebie.73/post-thread" , cookies=cookies, headers= header , data=form_data)
        print(r.status_code)
        for step in r.history:              
            print(step.status_code, step.headers.get("location"))
        if (r.status_code != 200):
            raise SystemError("change the cookies are dead")
        with open("logs.txt" , "a") as f:
            f.write(f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]\n")
            f.write(f"Status code: {r.status_code}\n")
            f.write(f"{r.content}\n")
            f.write("*" * 50 +"\”")
    sleep(random.randint(60 , 120))
