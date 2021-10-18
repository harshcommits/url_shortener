from flask import Flask, jsonify
import pyshorteners
import json

app = Flask(__name__)


@app.route('/check/<string:long_url>')
def check(long_url: str):

    with open('urls.txt', 'r') as file_data:
        file_json = json.load(file_data)
        short_url = file_json.get(long_url)

    if long_url in file_json.keys():
        return jsonify(message="Short URL: " + short_url)
    else:
        return jsonify(message='Data not present')


@app.route('/shorten/<string:long_url>', methods=['POST'])
def shorten(long_url: str):

    with open('urls.txt', 'a') as file:
        file_add = json.dumps(file)
        short_url = pyshorteners.Shortener.tinyurl.short(long_url)
        file_add.write({long_url: short_url})


if __name__ == '__main__':
    app.run()