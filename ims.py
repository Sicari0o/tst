import os
import sys
import hashlib
import subprocess
import requests
import time
import datetime

def removed():
    os.system('')
    try:
        httpCaht = requests.get("https://pastebin.com/raw/8YkXcL0K").text
        httpBand = requests.get("https://pastebin.com/raw/0wKNGXsK").text
        httpStop = requests.get("https://pastebin.com/raw/0wKNGXsK").text
        httpStop1 = requests.get("https://pastebin.com/raw/0wKNGXsK").text
        hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
        config = "$".join(hwid)
        id = hashlib.md5(config.encode("utf")).hexdigest()
        id = str(id)
        print("\nYour id >>> " + id + "\n")
        os.system('cls')
        if str(id) in httpBand:
            print("Your ID Has Been Banned" )
            time.sleep(5)
            sys.exit()

        elif str(id) in httpCaht:
            print("Your ID Has Been Activated")
            print(id)
            main()

        elif str(id) in httpStop:
            print("Your id >>> " + id)
            print(str(httpStop1))
            time.sleep(10)

        else:
            print("Your ID Not Activated >>> " + id )
            time.sleep(10)
            sys.exit()
    except:
        sys.exit()

def main():
    # TODO: Implement the main logic of your program here
    pass

if __name__ == "__main__":
    removed()
