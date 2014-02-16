# -*- coding: utf-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf8')
#import glob
#for file in glob.glob("*.txt"):
#    print file

def convertIP2(ip):
	#return '%d.%d' % (ip.split('.')[0],ip.split('.')[1]):
	return '.'.join((ip.split('.')[0],ip.split('.')[1]))

colname = ''
keyindex = 0
lastip = '';
with open("12-01flag.txt",'r') as file:
	for line in file:
	    words = line.split('\t')
	    if(colname == ''):
		colname = line
		i = 0
	    	for word in words:
	    		if(word == 'ip'):
	    			keyindex = i
	    			break
	    		i+=1
	    else:
	    	k = 0
	    	for word in words:
	    		if(k == keyindex):
	    			ip2 = convertIP2(word)
	    			with open(ip2+'.txt','a+b') as lf:
	    				lf.write(line)
	    		k+=1
