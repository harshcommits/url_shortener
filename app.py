from flask import Flask, jsonify, request, redirect, url_for
import os
import random

from url_short_test.url_short import short_url

app = Flask(__name__)

@app.route('/shorten/<string:longURL>')
def shorten(longURL: str):
    urlfile = open("url.txt", r)
    if longURL in urlfile:
        print ("value already present: " + urlfile[longURL])
    else:
        shortURL = url_for("short/" + random.randrange(100, 900))
        with open("url.txt", a) as add_url:
            add_url.write(shortURL)