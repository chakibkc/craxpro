import httpx as h
from bs4 import BeautifulSoup as bs
import random
from time import sleep
import json
from datetime import datetime
import pandas as pd 
from dotenv import load_dotenv
from config import tokens , headers_list
from getters import datagrap ,titlegrap
from validator import validate ,check_len
from credit import getcredit
import os

validate()

load_dotenv()

XFTOKEN = os.getenv("XFTOKEN")
COOKIES = json.loads(os.getenv("COOKIES"))
LINK = os.getenv("LINK")
PROFILE = os.getenv("PROFILE")

while(1):

    form_data = {
    "_xfToken": XFTOKEN,
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
        <p style="text-align: center;"> Statue : ✅ {datagrap()} From @check1ran_bot</p>
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
        r = Client.post(f"https://{LINK}/forums/freebie.73/post-thread" , cookies=COOKIES, headers= header , data=form_data)
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
    sleep(random.randint(70, 120))
    temp = check_len()
    if temp == 0:
        getcredit(LINK , PROFILE)
        break
    

