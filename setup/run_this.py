# installs pre-requisites for the project and creates a text file named token.txt in the same directory and writes the token in the file

import os
import subprocess
import sys
import time

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("discord.py")
install("asyncio")
install("datetime")

token = input("Enter your bot token: ")
with open("token.txt", "w") as f:
    f.write(token)
    f.close()
    print("Token saved in token.txt")
    time.sleep(2)

print("Setup complete")
