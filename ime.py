import subprocess
import hashlib
import time
import android
# Run the ADB command to get the IMEI
result = subprocess.check_output(["adb", "shell", "service", "call", "iphonesubinfo", "1"]).decode("utf-8")

# Extract the IMEI from the output
imei = result.split("'")[1]

# Compute the MD5 hash of the IMEI
md5_hash = hashlib.md5(imei.encode()).hexdigest()

# Print the hashed IMEI
print("This is your hashed IMEI (MD5):", md5_hash)
time.sleep(10)