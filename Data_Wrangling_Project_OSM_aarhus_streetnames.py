#MongoDB Wrangling
#Lesson 6 - Case Study : Openstreetmap Data
#Iterating through Ways Tags (#5)
#Example using xml.etree.ElementTree.iterparse

#import xml.etree.cElementTree as ET
import xml.etree.ElementTree as ET
from collections import defaultdict
import re
import pprint
from datetime import datetime

osm_file = open("aarhus_denmark.osm", "r")

# \b = word-boundary meta character (start-of-word). \B matches end-of-word
# \S = anything not a whitespace charcter (space, tab, newline, formfeed, and such). Opposite of \s
# + = quantyfier, at least one required, additional are optional
# \. = escaped metacharacter, matches the 'dot' character
# ? = quantyfier, one allowed, but it is optional
# $ = matches the position at the end of the string

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
street_types = defaultdict(set)
street_names = defaultdict(int)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", "Trail", "Parkway", "Commons"]

def aarhus_audit_street_name(street_name):
	#m = street_type_re.search(street_name)
	#if m:
		#street_type = m.group()
		#if street_type not in expected:
			#street_types[street_type].add(street_name)
	street_names[street_name] =+ 1

def print_sorted_dict(d):
	keys = d.keys()
	keys = sorted(keys, key=lambda s: s.lower())
	for k in keys:
		v = d[k]
		print "%s: %d" % (k,v)

def is_street_name(elem):
	return (elem.attrib['k'] == "name") #"addr:street")  #all the names are in the "name" attribute ... :-(

def audit():
	for event, elem in ET.iterparse(osm_file, events=("start",)):  # it's a tuple, remember the comma!
		if elem.tag == "way":
			for tag in elem.iter("tag"):
				if is_street_name(tag):
					#audit_street_type(street_types, tag.attrib['v'])
					aarhus_audit_street_name(tag.attrib['v'])
	pprint.pprint(dict(street_names))
#	pprint.pprint(dict(street_types))
#	print_sorted_dict(street_types)

if __name__ == '__main__':
	start = datetime.now()
	pprint.pprint(start)
	audit()
	end = datetime.now()
	pprint.pprint(end)
	pprint.pprint(start - end)

