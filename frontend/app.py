from flask import Flask
from flask import render_template, request

app = Flask(__name__, static_folder='static/js')

@app.route('/')
def hello_world():
    return render_template('index.html')

import binascii
@app.route('/send_back', methods=['POST'])
def receive_image():
    print('received image')
    image_str_raw = request.form['imgBase64']
    image_str = binascii.a2b_base64(image_str_raw.split(",")[1])
    with open('tmp.png', 'wb') as f:
      f.write(image_str)




    return 'image received'
    # return image
