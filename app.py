from flask import Flask, jsonify, request
import pyshorteners
import json
import os

app = Flask(__name__)


@app.route('/check', methods=['GET'])
def check():

    long_url = request.args.get('long_url')

    if os.stat('urls.txt').st_size != 0:
        with open('urls.txt', 'r') as file_data:
            file_json = json.load(file_data)
            short_url = file_json.get(long_url)

            if long_url in file_json.keys():
                return jsonify(message="Short URL: " + short_url)
            else:
                return jsonify(message='Data not present')

    else:
        return jsonify(message="The file is not readable")


@app.route('/shorten', methods=['POST'])
def shorten():

    long_url = request.args.get('long_url')
    short_url = pyshorteners.Shortener().tinyurl.short(long_url)

    with open('urls.txt', 'r') as file:
        file_json = json.load(file)
        file_json[long_url] = short_url

    with open('urls.txt', 'w') as file:
        #   file_json = {long_url: short_url}
        json.dump(file_json, file)
        return jsonify(message="New short URL created: " + short_url )


if __name__ == '__main__':
    app.run(DEBUG=True)