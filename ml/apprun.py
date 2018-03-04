# flask server
from betterPredict import predictcontext
import os
from random import *
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route("/findcontext",methods=['POST', 'GET'])
def findcontext():
	# if request.method=='POST':
	if request.method=='GET':
		url = str(request.args.get('url'))
		# url = request.form['url']
		response = dict()
		# response['context'] = 'water'
		context = predictcontext(url,9)
		print(url)
		print(context)
		response['context'] = context
		return jsonify(response)

@app.route("/addFilter",methods=['POST', 'GET'])
def addFilter():
	if request.method=='GET':
		filterList = str(request.args.get('filter'))
		fd = open("./userFilter.csv","a")
		fd.write(filterList)
		print("filter added successfully")
		return '', 204

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(port=8080,debug = True)
