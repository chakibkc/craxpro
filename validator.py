from getters import *

def check_len():
    with open("data/datacrax.txt", "r", encoding="utf-8") as f:
        l_data = sum(1 for _ in f)
    with open("data/titlecrax.txt", "r", encoding="utf-8") as r:
        l_title = sum(1 for _ in r)
    if (l_data != l_title):
        raise SystemError("the two files are not equal\n")
    if (l_data == l_title):
        leng = l_data
    return leng





def validate():
    print("Validation Started ...")
    check_len()
    getcookies()
    getxftoken()
    getlink()
    getprofile()
    print("Validation Done")