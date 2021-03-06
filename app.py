from socket import gethostname, gethostbyname 
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Home route that renders index.hmtl.
@app.route("/")
def index():
    return render_template("index.html")

# Route that returns some request header info.
@app.route("/api/whoami")
def who_is():
    
    ip = gethostbyname(gethostname())    
    data = request.headers.get('User-agent').split()
    soft = " ".join(data[1:6])
    lang = request.accept_languages[0][0]
    
    return jsonify(ipaddress=ip, language=lang, software=soft)

# Runs server
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8080)
