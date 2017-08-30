from flask import Flask, request
from flask_cors import CORS, cross_origin
import sys
sys.path.insert(0, 'style_transfer/src')
sys.path.insert(0, '.')
from style_transfer import evaluate #import ffwd_to_img
import binascii

app = Flask(__name__, static_folder='static/js')

cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
styles = ['rain_princess', 'scream', 'udnie', 'wave', 'wreck']
@app.route('/image', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])
def receive_image():
    print('received image')
    image_str_raw = request.form['imgBase64']
    style = request.form['style']
    print(style)
    if style not in styles:
        style ='scream'
    image_str = binascii.a2b_base64(image_str_raw.split(",")[1])
    with open('tmp.png', 'wb') as f:
      f.write(image_str)


    # TODO set checkpoint dir as an option
    evaluate.ffwd_to_img('tmp.png', 'processed.png', 'checkpoints/{}.ckpt'.format(style),
        device='/gpu:0')
    
    with open('processed.png', 'rb') as f:
        image_out = binascii.b2a_base64(f.read())
    return image_out
    # return image

@app.route('/')
def main_route():
    return render_template('index.html')
