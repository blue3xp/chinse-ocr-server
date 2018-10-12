#-*- coding:utf-8 -*-
import os
from flask import Flask, render_template, jsonify, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from deal import dealPicture

icon = UploadSet('PICTURE')

app = Flask(__name__)
app.config['UPLOADED_PICTURE_DEST']='test_images'
app.config['UPLOADED_PICTURE_ALLOWED']=IMAGES
app.config['JSON_AS_ASCII'] = False
configure_uploads(app, icon)

@app.route('/', methods=['GET'])
def picture():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    result_json = {
        'status': 'success',
        'message': ''
    }
    # print(request.files)
    request_json = request.files['file']
    filename = request_json.filename
    path = os.path.join(os.getcwd(), 'test_images')
    url = os.path.join(path, filename)
    if os.path.exists(url):
        os.remove(url)
    # store picture
    icon.save(request_json, name=filename)
    # deal with the picture in deal.py
    resultString = dealPicture(filename)
    result_json['message'] = resultString#.encode('utf-8').decode('utf-8')
    return jsonify(result_json)


myServerHost = '127.0.0.1'

if __name__ == '__main__':
    print("\n-------------the first run--------------------------")
    app.run(debug=False, host=myServerHost)
