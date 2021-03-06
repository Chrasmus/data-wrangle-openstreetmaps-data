#MongoDB Wrangling
#Lesson 6 - Case Study : Openstreetmap Data
#Iterative SAX XML Parsing (#3)
#Example using xml.etree.ElementTree.iterparse

import xml.etree.cElementTree as ET
#import xml.etree.ElementTree as ET
from collections import defaultdict
import re

osm_file = open("aarhus_denmark.osm", "r")

# \b = word-boundary meta character (start-of-word). \B matches end-of-word
# \S = anything not a whitespace charcter (space, tab, newline, formfeed, and such). Opposite of \s
# + = quantyfier, at least one required, additional are optional
# \. = escaped metacharacter, matches the 'dot' character
# ? = quantifier, one allowed, but it is optional
# $ = matches the position at the end of the string

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
street_types = defaultdict(int)

def audit_street_type(street_types, street_name):
	m = street_type_re.search(street_name)
	if m:
		street_type = m.group()
		street_types[street_type] += 1

def print_sorted_dict(d):
	keys = d.keys()
	keys = sorted(keys, key=lambda s: s.lower())
	for k in keys:
		v = d[k]
		print "%s: %d" % (k,v)

def is_street_name(elem):
	return (elem.tag == "tag") and (elem.attrib['k'] == "addr:street")

def audit():
	for event, elem in ET.iterparse(osm_file):
		if is_street_name(elem):
			audit_street_type(street_types, elem.attrib['v'])
	print_sorted_dict(street_types)

if __name__ == '__main__':
	audit()