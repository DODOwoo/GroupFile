import os
import glob
from bottle import *
import json

i = 0
onlyfiles = []
#@route('/')
#def index():
#	return template('index.html')
@route('/')
@view('index.tpl')
def indextpl():
	#print os.getcwd()
	onlyfiles = [ f for f in sorted(glob.glob("ip/*.json"), key=os.path.getsize, reverse=True) ]
	filename = onlyfiles[i]
	with open(filename,'r') as r:
		#content = json.load(r)
		content = ''
	return dict(filename=filename,content=content)

@route('/f/<fname>')
@view('index.tpl')
def filetpl(fname):
	with open('ip/'+fname,'r') as r:
		content = json.load(r)
	return dict(filename=fname,content=content)

@route('/changefile', method='POST')
def changeFile():
	fname = onlyfiles[++i]
	redirect('/f/%s' % fname)

@route('/s/<fname>')
def loads(fname):
	return static_file(fname, './s')

@route('/ip2/<fname>')
def loadfile(fname):
	return static_file(fname,'./ip2')

@route('/ip/<fname>',method='GET')
def loadfile(fname):
	return static_file(fname,'./ip')

@route('/ajax/getfiles.json',method='GET')
def getfiles():
	os.chdir('ip2')
	onlyfiles = [ f for f in glob.glob("*.txt") ]
	return json.dumps(onlyfiles)

@route('/ajax/getjsonfiles.json',method='GET')
def getfiles():
	os.chdir('ip')
	onlyfiles = [ f for f in glob.glob("*.json") ]
	return json.dumps(onlyfiles)

run(host='localhost', port=8097, debug=True)
