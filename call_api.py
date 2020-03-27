'''
This code is an example in the way we could use this api
command:
* proccess: to detect and get plate name and position on an image.
'''

import requests
import os
import json
import cv2

command="proccess"
face_name='monica'
ip_of_api="192.168.1.2"
port_of_api="5000"
path_image="/home/santi/Pictures/carro7_BAD.jpg"

# TO REGISTER FACES 
data = {
    'command':command, 
    'face_name':face_name
} 

frame=cv2.imread(path_image)
frame=cv2.imencode(".jpg", frame)[1]

### UPLOAD IMAGE 
files = {'json': (None, json.dumps(data), 'application/json'),
        'file': ('image.jpg', frame, 'multipart/form-data')}

response = requests.post(f'http://{ip_of_api}:{port_of_api}/file-upload',
                            files=files)