from flask import Flask, render_template
import json
import requests

app = Flask(__name__)


API_KEY = "3GbUdV4zjJXx0mGGoN3EooDwzLed4BFR" #Yes, I know it's my API key

@app.route("/", methods=["POST", "GET"])
def main():
    error = None
    url = requests.get(f"https://api.giphy.com/v1/gifs/trending?api_key={API_KEY}&limit=11")
    data = json.loads(url.text)
    list = []
    i = 0
    for _ in range(11):
        list.append(data["data"][i]["title"])
        i += 1

    #sep = " ".join(list)

    return render_template("index.html", content=list)

