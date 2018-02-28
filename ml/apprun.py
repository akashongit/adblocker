from predict import predictcontext
import os
from random import *
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route("/findcontext",methods=['POST', 'GET'])
def findcontext():
	if request.method=='POST':
	# if request.method=='GET':
		# url = str(request.args.get('url'))
		url = request.form['url']
		response = dict()
		# response['context'] = 'water'
		context = predictcontext(url)
		print(url)
		print(context)
		response['context'] = context
		return jsonify(response)

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(port=8080,debug = True)
