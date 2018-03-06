# flask server
from betterPredict import predictcontext
import os
from random import *
from flask import Flask, request
from flask import jsonify
from titleContextPredict import predictTitleContext
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/findcontext",methods=['POST', 'GET'])
def findcontext():
	# if request.method=='POST':
	if request.method=='GET':
		url = str(request.args.get('url'))
		# url = request.form['url']
		response = dict()
		# response['context'] = 'water'
		print(url)
		context1 = predictcontext(url)
		print(context1)
# title predict
		# r = requests.get(url)
		# data = r.text
		# soup = BeautifulSoup(data,"lxml")
		# title = soup.title.text
		# context2 = predictTitleContext(title)
		# print(context2)

		response['context'] = context1
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
