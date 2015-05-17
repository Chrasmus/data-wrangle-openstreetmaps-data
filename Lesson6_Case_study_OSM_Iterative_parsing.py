#MongoDB Wrangling
#Lesson 6 - Case Study : Openstreetmap Data
#Iterative Parsing (#3)
#Example using xml.etree.ElementTree.iterparse

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.ElementTree as ET
import pprint
from collections import defaultdict

tags = defaultdict(int)

def count_tags(filename):
    # YOUR CODE HERE
    for event, elem in ET.iterparse(filename):
        #pprint.pprint(elem.tag, elem.text)
        tags[elem.tag] += 1

    pprint.pprint(tags)
    return tags

def test():

    tags = count_tags('aarhus_denmark.osm')
    pprint.pprint(tags)
    

if __name__ == "__main__":
    test()

# RESULT

# defaultdict(<type 'int'>, {'node': 392219, 'nd': 384879, 'bounds': 1, 'member': 3679, 'tag': 1134299, 'relation': 435, 'way': 47016, 'osm': 1})
