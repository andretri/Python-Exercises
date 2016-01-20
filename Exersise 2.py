import urllib2
import json

D = raw_input("> Enter Date (dd-mm-yyyy): ")
json_file = urllib2.urlopen(("http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json")%(D))
text = json.load(json_file)

Numbers = {x:0 for x in range(1,81)}

listlength = len(text["draws"]["draw"])
for i in range(listlength):
	for j in text["draws"]["draw"][i]["results"]:
		#print text["draws"]["draw"][i]["results"]		//[FOR DEBUGGING PURPOSES]
		Numbers[j] += 1
		#print j		//[FOR DEBUGGING PURPOSES]
	#print "\n"			//[FOR DEBUGGING PURPOSES]

for i in range(1,81):
	print (i),":",Numbers[i]
