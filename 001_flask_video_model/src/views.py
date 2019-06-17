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
    n = countCameras()
    return render_template('index.html',data=n)

def clearCapture(capture): 
    capture.release() 
    cv2.destroyAllWindows() 
    
@app.route('/countCameras')
def countCameras(): 
    n = 0 
    for i in range(10): 
     try: 
      cap = cv2.VideoCapture(i) 
      ret, frame = cap.read() 
      cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
      clearCapture(cap) 
      n += 1 
     except: 
      clearCapture(cap) 
      break 
    return n

def get_video():
    video_reader = cv2.VideoCapture(0)
    video_reader.set(3, 640)


    while True:
        ret, image = video_reader.read()

        ret, jpeg = cv2.imencode('.jpg', image)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

def get_video2():
    video_reader = cv2.VideoCapture(1)
    video_reader.set(3, 640)


    while True:
        ret, image = video_reader.read()

        ret, jpeg = cv2.imencode('.jpg', image)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
def get_video3():
    video_reader = cv2.VideoCapture(2)
    video_reader.set(3, 640)


    while True:
        ret, image = video_reader.read()

        ret, jpeg = cv2.imencode('.jpg', image)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
def get_video4():
    video_reader = cv2.VideoCapture(3)
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

@app.route('/detect_video2')
def detect_video2():
    return Response(get_video2(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detect_video3')
def detect_video3():
    return Response(get_video3(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detect_video4')
def detect_video4():
    return Response(get_video4(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')