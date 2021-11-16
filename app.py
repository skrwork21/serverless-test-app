# app.py

from datetime import datetime
from flask import Flask, render_template, jsonify, send_file, request, Response
import os
import io
import base64
import boto3
import json
import numpy

app = Flask(__name__, static_url_path='', static_folder='static/assets/')

@app.route("/hello")
def hello():
    return Response("world", mimetype="application/json")
