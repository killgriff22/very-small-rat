from netifaces import interfaces, ifaddresses, AF_INET
import requests, commandhandler
def connect():
    addresses=[]
    for ifaceName in interfaces():
        addresses.append([i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )])
    res = []
    for i in addresses:
        if (i not in res):
            if not i[0] in 'No IP addr':
                if not i[0] in '127.0.0.1':
                    res.append(i[0])
    addresses=res
    res=[]
    for addr in addresses:
        res.append(f'http://{addr}:3090')
    addresses=res
    for i in range(len(addresses)):
        print(f'[{i+1}] {addresses[i]}')
    print(f'[{i+2}] manually enter ip')
    ans = input('enter the ID of the address you want to connect to: >>')
    ans = int(ans)-1
    if ans > len(addresses):
        print("please enter a valid address ID")
        exit()
    if ans == len(addresses):
        inp = input('Enter the address you want to connect to >>')
        if "http://" in inp or "https://" in inp:
            if ".co" in inp or ".net" in inp:
                try:
                    int(inp[len(inp)-1:])
                    int(inp[:len(inp)-1])
                except:0

        inp = f'http://{inp}:3090'
        resp = requests.get(f"{inp}/status")
        connected = True
        address = inp
    else:
        resp = requests.get(f"{addresses[ans]}/status")
        connected = True
        address = addresses[ans]
    if resp.text == "READY FOR COMMAND":
        print(f"connected to {address}")
        while connected:
            try:requests.get(f"{address}")
            except:exit()
            command = input(">>")
            resp = requests.post(f"{address}/commands/exec?command={command}")
            commandhandler.execute(command,address)
            print(resp)
while 1:
    connect()
    connect()
    connect()