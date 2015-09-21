import re
import lxml.html as lh
import urllib
import urllib2
from HTMLParser import HTMLParser


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

i_no=str('0136276')

response = urllib2.urlopen("http://webapps6.doc.state.nc.us/opi/viewoffender.do?method=view&offenderID="+str(i_no))
the_page = re.sub('\r','',response.read())
the_page = re.sub('\n','',the_page)
the_page = re.sub('\t','',the_page)
print the_page
profile = re.sub('\'','',strip_tags(the_page))
profile = re.split(',',profile)
#profile = filter(None, profile)
profile = filter(lambda x: not re.match(r'^\s*$', x), profile)

for i in range(len(profile)):
	if profile[i]==" Offender Information": print "Prisoner Name\t\t:\t\t"+str(profile[i+1])
	if profile[i]==" Inmate Status:": print "Inmate Status\t\t:\t\t"+str(profile[i+1])
	if profile[i]==" Current Location:": print "Current Location\t\t:\t\t"+str(profile[i+1])+"\n\n"
