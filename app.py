from flask import Flask, jsonify, request, redirect
import random
import string
import json
import os

app = Flask(__name__)


@app.route('/check', methods=['GET'])
def check():

    long_url = request.args.get('long_url')

    if os.stat('urls.txt').st_size != 0:
        with open('urls.txt', 'r') as file_data:
            file_json = json.load(file_data)

            invert_json = {v: k for k, v in file_json.items()}

            if long_url in invert_json:
                short_url = invert_json[long_url]
                return jsonify(message="Short URL: http://localhost:5000/" + short_url + " exists")
            else:
                return jsonify(message="this URL does not exist")

    else:
        return jsonify(message="The file is not readable")


@app.route('/shorten', methods=['POST'])
def shorten():

    long_url = request.args.get('long_url')

    content = string.ascii_lowercase + string.digits
    short_url = random.choices(content, k=6)
    short_url = "".join(short_url)

    with open('urls.txt', 'r') as file:
        file_json = json.load(file)
        file_json[short_url] = long_url

    with open('urls.txt', 'w') as file:
        #   file_json = {short_url: long_url}
        json.dump(file_json, file)
        return jsonify(message="New short URL created: http://localhost:5000/" + short_url)


@app.route('/<string:short_url>')
def redirect_short(short_url: str):

    with open('urls.txt', 'r') as file:
        file_json = json.load(file)

        if short_url in file_json.keys():
            long_url = file_json.get(short_url)
            return redirect(long_url)
            # return jsonify(long_url)
        else:
            return jsonify(message="URL does not exist")


if __name__ == '__main__':
    app.run()
