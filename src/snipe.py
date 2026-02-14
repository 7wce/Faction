import requests as r
import time
from colorama import init
from genusername import gen

init()

robloxApi = "https://auth.roblox.com/v1/usernames/validate"

def trySniping(username, xcsrf):
    if not username:
        return "No username set."
    if not xcsrf:
        return "No x-csrf-token sent."

    headers = {
        "X-Csrf-Token": xcsrf or None,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Referer": "https://www.roblox.com/"
    }

    payload = {
        "birthday": "2003-11-08T17:00:00.000Z",
        "context": "Signup",
        "username": username
    }

    try:
        response = r.post(robloxApi, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data.get("code") == 0 and data.get("message") == "Username is valid":
            return True
        else:
            return False

    except r.exceptions.RequestException as e:
        print("Request failed:", e)
        return False
    
def snipeLoop(loop, option, token):
    if not loop or not option:
        return False

    gotUsernames = []

    option_map = {
        1: "four",
        2: "five",
        4: "random",
        5: "lnb"
    }

    if option == 3:
        return []

    gen_type = option_map.get(option)
    if not gen_type:
        return []

    for a in range(loop):
        time.sleep(1)
        username = gen(gen_type)
        print(f"\033[38;2;217;217;0m    Trying out username `{username}`")
        if trySniping(username, xcsrf=token):
            gotUsernames.append(username)
            print(f"\033[38;2;0;217;105m    Username `{username}` hadn't been claimed.")
        else:
            print(f"\033[38;2;217;0;83m    Username '{username}' has been claimed.")

    return gotUsernames