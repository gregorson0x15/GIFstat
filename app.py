from flask import Flask
import json
import requests

app = Flask(__name__)


API_KEY = "Your Giphy API"

@app.route("/", methods=["POST", "GET"])
def main():
    error = None
    url = requests.get(f"https://api.giphy.com/v1/gifs/trending?api_key={API_KEY}&limit=11")
    data = json.loads(url.text)
    title0 = data["data"][0]["title"]
    title1 = data["data"][1]["title"]
    title2 = data["data"][2]["title"]
    title3 = data["data"][3]["title"]
    return [title0, title1, title2, title3]

