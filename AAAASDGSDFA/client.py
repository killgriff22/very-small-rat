import requests
while True:
    inp=input("input command to execute:\n>>")
    requests.post("https://BraveVelvetyCrash.killergriffn.repl.co/commands/toexec?command="+inp)