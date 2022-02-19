# there wasnt really a "source code" to this but

import requests
import json
import os
import time

newinput = input
newprint = print
ask4pass = "password:"
sleep = time.sleep
get = requests.get

incorrect = "incorrect password, retry\n"
correct = "good job you got it correct.\nclosing."

link1 = "https"
link2 = "://"
link3 = "paste"
link4 = "bin.com"
link5 = "/raw/"
link6 = "4JanPfiQ"

fullink = get(link1+link2+link3+link4+link5+link6).json()
key = fullink["IlIlIlIlIlllIlllI"]+fullink["IlIlIlIlIlIlIlIlI"]+fullink["IlIIIlIlIlIlIlllI"]
# print(key) # You can use this to print out they key

def passsys():
    inputkey = newinput(ask4pass)
    if inputkey == key:
        newprint(correct)
        sleep(1)
    else:
        print(incorrect)
        passsys()
passsys()