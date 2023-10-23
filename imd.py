import os
import hashlib
import requests
import time
import android

def removed():
    droid = android.Android()
    
    try:
        # Replace this with the actual URLs of your Pastebin data
        httpCaht = requests.get("https://pastebin.com/raw/8YkXcL0K").text
        httpBand = requests.get("https://pastebin.com/raw/0wKNGXsK").text

        # Get the device's serial number
        serial_number = droid.readPhoneInfo().result["serial"]

        # Calculate the MD5 hash of the serial number
        id = hashlib.md5(serial_number.encode("utf")).hexdigest()

        id = str(id)
        print("\nYour id >>> " + id + "\n")
        os.system('clear')  # Use 'clear' for Termux, 'cls' is for Windows

        if str(id) in httpBand:
            print("Your ID Has Been Banned" )
            time.sleep(5)
            sys.exit()
        elif str(id) in httpCaht:
            print("Your ID Has Been Activated")
            print(id)
            main()
        else:
            print("Your ID Not Activated >>> " + id)
            time.sleep(10)
            sys.exit()
    except:
        sys.exit()

def main():
    # TODO: Implement the main logic of your program here
    pass

if __name__ == "__main__":
    removed()
