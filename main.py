import string
import random
import requests
import capmonster_python.turnstile
import threading


def genkey():
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(6))
    return random_string


def bypass():
    capmonster = capmonster_python.turnstile.TurnstileTask("")
    task_id = capmonster.create_task("https://ryo.sh", "0x4AAAAAAAOE-pbn1T-JGNjg") 
    result = capmonster.join_task_result(task_id)
    print("SOLVE " + result.get("token")[:50])
    
    response = requests.post(F"https://ryo.sh/download_token.php?token={genkey()}", headers={
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }, data={
        "cf-turnstile-response": result.get("token")
    })
        
    if "Invalid token" in response.text:
        print(f"Invalid Electron Key: {response.url}")
    else:
        print(f"Correct Key {response.url}")
        exit(0)


threads = []
for _ in range(10): 
    thread = threading.Thread(target=bypass)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()