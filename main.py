import requests, random, time
from colorama import Fore

while True:
    user = ""
 
    for character in random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=3):
        user = user + character
 
    response = requests.get(f"https://instagram.com/{user}/")

    if (response.status_code == 400): #400 means it's valid
        print(Fore.RED + f"INVALID: {user}" + Fore.RESET)
    elif (response.status_code == 404): # 404 is the error code
        print(Fore.GREEN + f"VALID: {user}" + Fore.RESET)

    else:
        print("BLOCKED")
        time.sleep(120)
