from flask import Flask, jsonify, request, redirect, url_for
import os
import random

app = Flask(__name__)

@app.route('/shorten/<string:longURL>')
def shorten(longURL: str):
    urlfile = open("url.json", 'r')
    if longURL in urlfile:
        print ("value already present: " + urlfile[longURL])
    else:
        shortURL = url_for("short/" + random.randrange(100, 900))
        with open("url.json", 'a') as add_url:
            add_url.write(shortURL)

@app.route('/<shortURL>')
def redirect_long(shortURL):
    url_ref = open("url.json", 'r')
    if shortURL in url_ref:
        return redirect(url_ref.key[shortURL])