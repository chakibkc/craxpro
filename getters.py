from dotenv import set_key , load_dotenv
import os


load_dotenv()


def getcookies():
    cookies = os.getenv("COOKIES")
    if cookies == "":
        var = input("Enter Your Cookies")
        set_key(".env" , "COOKIES" , var)
    



def getxftoken():
    xf = os.getenv("XFTOKEN")
    if xf == "":
        var = input("Enter Your XF-TOKEN")
        set_key(".env" , "XFTOKEN" , var)
    

def getlink():
    link = os.getenv("LINK")
    if link == "":
        var = input("Enter Your Link without HTTPS")
        set_key(".env" , "LINK" , var)

def getprofile():
    link = os.getenv("PROFILE")
    if link == "":
        var = input("Enter Your PROFILE USER")
        set_key(".env" , "PROFILE" , var)


def datagrap():
    with open("data/datacrax.txt","r") as r:
        lines = r.readlines()
        if(len(lines)==0):
            raise SystemError("Data Completed")
        if not lines:
            raise SystemError("the file is empty check the file again\n")
        st_line = lines[0].strip()
    with open("data/datacrax.txt" , "w") as r:
        r.writelines(lines[1:])
    return st_line

def titlegrap():
    with open("data/titlecrax.txt","r") as r:
        lines = r.readlines()
        if(len(lines)==0):
            raise SystemError("Data Completed")
        if not lines:
            raise SystemError("the file is empty check the file again\n")
        st_text = lines[0].strip()
    with open("data/titlecrax.txt" , "w") as r:
        r.writelines(lines[1:])
    return st_text
