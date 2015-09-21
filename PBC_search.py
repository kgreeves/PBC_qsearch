import sys
sys.path.append("./MOD")

import re
import lxml.html as lh
import urllib
import urllib2
from HTMLParser import HTMLParser
from getData import *



class MyHTMLParser(HTMLParser):

    	def __init__(self):
		self.reset()
		self.fed = []

	def handle_data(self, data):
		self.fed.append(data) 
	def get_data(self):
		return list(self.fed)
		return ''.join(self.fed)

def strip_tags(html):
	s = MyHTMLParser()
	s.feed(html)
	return str(s.get_data())

def run_query(i_no):
	response = urllib2.urlopen("http://webapps6.doc.state.nc.us/opi/viewoffender.do?method=view&offenderID="+str(i_no)+"&summary=Y")
	the_page = re.sub('\r','',response.read())
	the_page = re.sub('\n','',the_page)
	the_page = re.sub('\t','',the_page)

	#print the_page
	profile = re.sub('\'','',strip_tags(the_page))
	profile = re.split(',',profile)
	profile = filter(lambda x: not re.match(r'^\s*$', x), profile)
	

	print chr(27) + "[2J"
	print "-------------------------------------------------------------------"
	print "Prisoner ID: "+str(i_no)+" (Short Record) "
	print "-------------------------------------------------------------------"
	
	OIbool=ISbool=CLbool=0;iStatus=""	
	for i in range(len(profile)):
		if profile[i]==" Offender Information" and OIbool==0:
			pName=str(profile[i+1])
			print "\nPrisoner Name\t\t:\t\t"+pName
			OIbool=1
		if profile[i]==" Inmate Status:" and ISbool==0:
			iStatus=str(profile[i+1])
			print "Inmate Status\t\t:\t\t"+iStatus
			ISbool=1
		if profile[i]==" Current Location:" and CLbool==0:
			cLoc=str(profile[i+1])
#			print "Current Location\t:\t\t"+cLoc+"\n\n"
			CLbool=1
		
	if iStatus==" ACTIVE": print "Current Location\t:\t\t"+cLoc+"\n\n"
	
	if iStatus == " ACTIVE":
		parts = cLoc.split(' ')	
		sp= " ";found = 0;
		for n in range(len(mailto)/3):
			if mailto[3*n][0] == parts[1]:
				print "Mail to:"
				print "\t\t"+pName.upper()+" - "+i_no
				print "\t\t"+cLoc
				print "\t\t "+sp.join(mailto[3*n+1])
				print "\t\t "+sp.join(mailto[3*n+2])+"\n\n\n"
				found=1; break
		if found==0:
			print "Mail to:"
			print "\t\tUnable to locate address for "+cLoc+"\n\n\n" 


	print "-------------------------------------------------------------------"
	print "					'exit' or 'quit' to escape"
	






#%%%%
#MAIN
#%%%%%

lu=""

mailto = getData("./MOD/prison_add.dict",1)

while lu != "exit" and lu != "Exit" and lu != "quit" and lu != "Quit" and lu !="q" and lu != "Q":
	i_no=raw_input("\n\n\n\n\nPrisoner ID:")
	run_query(i_no)
	lu=raw_input()
#print "\n\n\n\n\nPrisoner ID:"

