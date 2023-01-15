import time
import subprocess

phone_number = "1234567890" #replace with the desired number


while True:
    subprocess.call(["telnet", phone_number])
    time.sleep(5)
