import os
import urllib.request
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

from lpr import *
import json


app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_busy():

	with open('src/database.json','r') as json_file:
		data = json.load(json_file)	
	if(data['flag_occupied']=="BUSY"):
		return True
	else:
		with open('src/database.json','w') as json_file:
			data['flag_occupied']="BUSY"
			json.dump(data, json_file)
		return False
	
def not_busy():
	with open('src/database.json','r') as json_file:
		data = json.load(json_file)
	
	with open('src/database.json','w') as json_file:
		data['flag_occupied']="NOT BUSY"
		json.dump(data, json_file)

	print("NOT BUSY")
		
@app.route('/update_model/', methods=['GET'])
def update_model():
	
	if is_busy():	
		resp = jsonify({'message': 'Service is being used'})
		resp.status_code = 400
		return resp

	proccess_data()
	resp = jsonify({'message': 'Successfully trained'})
	resp.status_code = 200
	not_busy()
	return resp

@app.route('/file-upload/', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	json_params=json.loads(request.form['json'])

	
	if is_busy():	
		resp = jsonify({'message': 'Service is being used'})
		resp.status_code = 400
		return resp

	if 'command' in json_params:

		if 'file' not in request.files:
			resp = jsonify({'message': 'No file part in the request'})
			resp.status_code = 400
			not_busy()
			return resp

		file_1 = request.files['file']

		if file_1.filename == '':
			resp = jsonify({'message': 'No file selected for uploading'})
			resp.status_code = 400
			not_busy()
			return resp

		if file_1 and allowed_file(file_1.filename):
			filename = secure_filename(file_1.filename)

			file_1.save(os.path.join("./", filename))
			img=cv2.imread(f"./{filename}")

			if json_params['command']=='proccess':
				detections=do_detect(img)
				print("\ndetections")
				print(detections)
				resp = jsonify({'message' : detections})
				resp.status_code = 201
				not_busy()
				return resp
			else:
				resp = jsonify({'message' : 'Command unrecognized'})
				resp.status_code = 400
				not_busy()
				return resp

		else:
			resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
			resp.status_code = 400
			not_busy()
			return resp


	else:

		resp = jsonify({'message' : 'BAD USAGE, tell command.'})
		resp.status_code = 400

		not_busy()
		return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')

    

