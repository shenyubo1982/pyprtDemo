from flask import Flask, request, render_template
from flask_cors import *
import json
import time
import copy
import random
import os

import customerDemo

app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r'/*')

CORS(app)

# json 文件读取
with open('./table.json', 'r+') as f:
    data = json.loads(f.read())


@app.route('/')
def index():
    # return 'Hello,Python Flask!'
    return render_template('index.html')


@app.route('/api/name')
def name():
    return 'Name: Leif'


@app.route('/api/info', methods=['GET'])
def info():
    type = request.args.get('type')
    time = request.args.get('time')
    print('type: ' + type + '\n' + 'time: ' + time)
    return json.dumps({'Name': 'Leif', 'age': 23, 'job': 'Programmer'})


@app.route('/api/info', methods=['POST'])
def setInfo():
    return json.dumps({'retcode': 0, 'msg': 'Set info success!'})


@app.route('/api/params', methods=['POST'])
def params():
    # browser & os & computer & folder
    browser = request.form.get('browser')
    os = request.form.get('os')
    computer = request.form.get('computer')
    folder = request.form.get('folder')
    print('browser: ' + browser + '\n' +
          'os: ' + os + '\n' +
          'computer: ' + computer + '\n' +
          'folder: ' + folder)
    return json.dumps({'retcode': 0, 'msg': 'Post params success!'})


# 图片上传
@app.route('/api/pic', methods=['POST'])
def pic():
    img = request.files.get('file')
    if img is None:
        return json.dumps({'msg': 'File upload fail!'})
    else:
        img.save(img.filename)
        return json.dumps({'msg': 'File upload success!'})


@app.route('/api/stcode')
def statusCode():
    return json.dumps({'retcode': 0}), 411


@app.route('/api/json')
def getJson():
    return json.dumps(data)


@app.route('/api/play', methods=['GET'])
def play():
    filename = request.args.get('filename')
    customerDemo.playDemo(filename)
    return json.dumps({'File': filename, 'Status': 'Success'})


app.run(debug=True, host='0.0.0.0', port=8000)
