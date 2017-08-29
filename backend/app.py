from flask import Flask
from flask import request
from style_transfer import ffwd_to_img
app = Flask(__name__, static_folder='static/js')

import binascii
@app.route('/image', methods=['POST'])
def receive_image():
    print('received image')
    image_str_raw = request.form['imgBase64']
    image_str = binascii.a2b_base64(image_str_raw.split(",")[1])
    with open('tmp.png', 'wb') as f:
      f.write(image_str)


    # TODO set checkpoint dir as an option
    ffwd_to_img('tmp.png', 'tmp/', 'checkpoints/',
        device='/gpu:0')
    return 'image received'
    # return image
