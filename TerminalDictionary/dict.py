import argparse
import sys
import urllib.request    #library for fetching internet resources
import json      #library for json operations

def processCommandline():
	parser = argparse.ArgumentParser()
	parser.add_argument("-w",help="Enter the word to be searched")

	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit(1)
	args = parser.parse_args()
	return args


args = processCommandline()
print("Word: ",args.w)
#stores the json formatted output to a variable
url = 'http://glosbe.com/gapi/translate?from=eng&dest=eng&\
format=json&phrase='+args.w+'&pretty=true'
 
#json representation of url is stored in variable result
result = json.load(urllib.request.urlopen(url)) 
 
#get the first text in "meaning" in "tuc" from result
print("Meaning: ", result["tuc"][0]["meanings"][0]["text"])
