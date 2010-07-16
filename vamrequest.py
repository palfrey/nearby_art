#!/usr/bin/env python
import cgi
import traceback
form = cgi.FieldStorage()

print "Content-Type: text/plain"
print

try:
	exception = BaseException
except NameError: # python <2.5
	exception = Exception

try:
	from urllib import urlopen
	obj = bool(int(form.getfirst("obj","0")))
	if obj:
		id = form.getfirst("id", "0")
		url = "http://www.vam.ac.uk/api/json/museumobject/"+id
	else:
		lat = float(form.getfirst("lat", "0"))
		lon = float(form.getfirst("lon", "0"))
		url = "http://www.vam.ac.uk/api/json/museumobject/search?latitude=%.6f&longitude=%.6f&radius=50&orderby=distance"%(lat, lon)

	data = urlopen(url)
	print data.read()
except exception, e:
	tr = traceback.format_exc()
	print "<pre>%s</pre>"%tr
