import flask
import lipd
import json
from flask import Flask
from flask import send_from_directory
from flask import request
from lipd import readLipd

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def receiveLiPD():
   input = json.loads(request.files['parameters'].read())
   parameters = input['parameters']
   file_names = input['inputFiles']

   # read the input lipd files
   input_lipds = {}
   for file_name in file_names:
      file = request.files[file_name]
      file.save(file_name)
      input_lipds[file_name] = lipd.readLipd("./" + file_name)
   
   # here we would pass parameters & input_lipds to the climate model
   print(parameters)
   print(input_lipds)

   # fake NetCDF file that would really come from the climate model
   return send_from_directory("./", "test.nc")


# setting the host and port for the server to run on
app.run(host='0.0.0.0', port=80)
