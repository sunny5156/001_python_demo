#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, sys,time
from flask import Flask, render_template, Blueprint,Response
import cv2

app = Flask(__name__)
main = Blueprint('main', __name__)
app.register_blueprint(main,url_prefix = "")

@app.route('/')
def index():
    return render_template('index.html')


def get_video():
    video_reader = cv2.VideoCapture(0)
    video_reader.set(3, 640)


    while True:
        ret, image = video_reader.read()

        ret, jpeg = cv2.imencode('.jpg', image)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/detect_video')
def detect_video():
    return Response(get_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
