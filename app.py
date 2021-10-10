from flask import Flask, jsonify

@app.route('/shorten')
def shorten():
    shortURL = open("url.txt", r)
    for line in shortURL:
        if 