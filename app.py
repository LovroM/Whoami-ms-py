from flask import Flask, render_template, jsonify
from socket import gethostname, gethostbyname 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/whoami")
def who_is():
    
    ip = gethostbyname(gethostname())    

    return jsonify(ipaddress = ip, language = "def sl-SI", software = "def Windows NT 10.0; Win64; x64")


### Runs server
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8080)