from flask import Flask,request,render_template
from onnx_classifier import *

app = Flask(__name__)

@app.route('/classify_mask',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        validation = 'Please Use Postman or Python Script to Send Base64 Image'
        return validation
    
    elif request.method == 'POST':
        data_json   = request.json
        img_data = data_json["image"]
        response = predict(img_data)
        response = list(response)
        # print(response)
        return 'class={} ; probability={}'.format(response[0], response[1])

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
