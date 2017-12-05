
# coding: utf-8

# In[1]:

#counting the no.of unique tags in a selected XML file.

import xml.etree.cElementTree as ET
from collections import defaultdict

def no_of_tags(osmfile):
    tags = defaultdict(int)
    for event, elem in ET.iterparse(osmfile):
        tags[elem.tag] +=1
    return tags    


# In[3]:

import re
import pprint
OSMFILE = "p3dallas_texas.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
print no_of_tags(OSMFILE)

