import os
import requests
import time

os.system("title very lame password system")
I = "https"
II = "://"
III = "pastebin.com"
IV = "/raw/"
V = "4JanPfiQ"
VI=I+II+III+IV+V
VII=requests.get(VI).json()
jj=VII["I"]+VII["II"]+VII["III"]

def trycrack():
    inputpass = input("Password: ")
    if inputpass != jj:
        print("incorrect password, retry\n")
        trycrack()
    elif inputpass == jj:
        print("good job you got it correct.\nclosing.")
        time.sleep(2)

trycrack()