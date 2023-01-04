# installs pre-requisites for the project and creates a text file named token.txt in the same directory and writes the token in the file

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
print("""\n \n \n run the bot by running the run.py file MAKE SURE TO ANABLE ALL INTENTS IN THE DISCORD DEVELOPER PORTAL.

When the bot is running use .setup to setup the bot""")
time.sleep(20)



