import os
os.system("python3 -m pip install flask")
from flask import Flask
import flask
app = Flask(__name__)
toexec=[]
@app.route("/status")
def status():
    if flask.request.method == "GET":
        return "READY FOR COMMAND"
@app.route("/commands/toexec",methods=["POST"])
def toexecute():
    toexec.append(flask.request.args.get("command"))
    return "OK"
@app.route("/commands/exec",methods=["POST"])
def execute():
    tmp=toexec
    toexec=[]
    return str(tmp)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3090, debug=False)