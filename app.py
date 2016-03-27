from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/whoami")
def who_is():
    

    return jsonify(ipaddress = "62.42.167.183",language = "sl-SI", software = "Windows NT 10.0; Win64; x64")


### Runs server
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8080)