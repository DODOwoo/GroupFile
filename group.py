# -*- coding: utf-8 -*-
# coding=utf-8
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import json
#import glob
#for file in glob.glob("*.txt"):
#    print file

def convertIP2(ip):
	#return '%d.%d' % (ip.split('.')[0],ip.split('.')[1]):
	return '_'.join((ip.split('.')[0],ip.split('.')[1]))

colname = {}
content = {}
keyindex = 0
lastip = '';
with open("12-01flag.txt",'r') as file:
	for line in file:
	    words = line.split('\t')
	    if(len(colname) == 0):
		i = 0
		for word in words:
			colname[i] = word.decode('utf-8').encode('utf-8')
			print i,colname[i]
	    		if(word == 'ip'):
	    			keyindex = i
			i += 1
		with open('s/coltitle.json','a+b') as tf:
			json.dumps(colname, tf)
	    else:
	    	k = 0
	    	for word in words:
			content[colname[k]] = word.decode('utf-8').encode('utf-8')
	    		k+=1
		k = 0
	    	for word in words:
	    		if(k == keyindex):
	    			ip2 = convertIP2(word)
	    			with open('ip/'+ip2+'.json','a+b') as lf:
	    				json.dumps(content,lf)
				break
	    		k+=1
