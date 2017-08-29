from flask import Flask
from flask import request

app = Flask(__name__, static_folder='static/js')

import binascii
@app.route('/image', methods=['POST'])
def receive_image():
    print('received image')
    image_str_raw = request.form['imgBase64']
    image_str = binascii.a2b_base64(image_str_raw.split(",")[1])
    with open('tmp.png', 'wb') as f:
      f.write(image_str)




    return 'image received'
    # return image
