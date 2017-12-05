
# coding: utf-8

# In[2]:

import schema 
SCHEMA = schema.schema


# In[14]:

#auditing and cleaning for the dallas osm file.
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "p3dallas_texas.osm"  # impoorting the .osm file from the folder
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Texas","Dallas","Richardson","Street", "Avenue", "Boulevard", "Drive", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway"]

# changing the variables in to new names
mapping = { "TX" : "TEXAS",
           "dallas":"Dallas",
            "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
             "Dr.": "Drive",
            "Blvd" : "Boulevard",
            "Dr" : "Drive",
            "W"  :"West",
            "way" :"Way"
            }


def audit_street_type(street_types, street_name): 
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def uppercase(i): #it is used to captalize the letters.
    if i.isuppercase:
        return i
    else:
        return i.title()


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    
    return street_types
pprint.pprint(dict(audit(OSMFILE)))
# overabbrivating the street names

def update_name(OSMFILE): # overabbrivating the street names
    update = []
    for splitting  in name.split(' '):
        if splitting in mapping.keys():
            splitting = mapping[splitting]
        update.append(splitting)
    return " ".join(update)

    update_street = audit(OSMFILE)
    for street_type, ways in update_street.iteritems():
        for name in ways:
            if street_type in mapping:
                better_name = name.replace(street_type, mapping[street_type])
                print name, "=>", better_name  
                

                
                
                
new_name = update_name(OSMFILE)
print new_name


# In[8]:

print len(audit(OSMFILE))


# In[36]:

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
#auditing the postal codes from the data


def audit_zipcode(postcode_file):
    osmfile = open(postcode_file,"r")
    codes =set()
    s_code =0
    for event, elem in ET.iterparse(osmfile,events = ("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:postcode":
                    if len(tag.attrib['v']) >5:
                        s_code +=1
                        tag.attrib['v'] = tag.attrib['v'].split('_')[0]
                    codes.add(tag.attrib['v'])
    print "The long codes are:",s_code,'long post codes.'
    return [code for code in codes if code not in dallas_tx]
    


# In[37]:

OSMFILE = "p3dallas_texas.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
postcode_file = audit_zipcode(OSMFILE)
print len(postcode_file)


# In[ ]:




# In[1]:

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "p3dallas_texas.osm"  # impoorting the .osm file from the folder
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Texas","Dallas","Richardson","Street", "Avenue", "Boulevard", "Drive", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway"]

# changing the variables in to new names
mapping = { "TX" : "TEXAS",
           "dallas":"Dallas",
            "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
             "Dr.": "Drive",
            "Blvd" : "Boulevard",
            "Dr" : "Drive",
            "W"  :"West",
            "way" :"Way"
            }


def audit_street_type(street_types, street_name): 
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def uppercase(i): #it is used to captalize the letters.
    if i.isuppercase:
        return i
    else:
        return i.title()


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    
    return street_types
pprint.pprint(dict(audit(OSMFILE)))
# overabbrivating the street names

def update_name(name, mapping): # overabbrivating the street names
    update = []
    for splitting  in name.split(' '):
        if splitting in mapping.keys():
            splitting = mapping[splitting]
        update.append(splitting)
    return " ".join(update)


update_street = audit(OSMFILE) 

for street_type, ways in update_street.iteritems():

    for name in ways:

        better_name = update_name(name, mapping)

        print name, "=>", better_name  


# In[38]:

print postcode_file


# In[8]:

def cities(no_of_cities):# extracting the cities from the .osm file downloaded
    osmfile = open (no_of_cities,"r")
    city = set()
    for event, elem in ET.iterparse(osmfile, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:city" and tag.attrib['v'] != "dallas":
                    city.add(tag.attrib['v'])
    return city          


# In[43]:

city = cities(OSMFILE)
print len(city)


# In[9]:

city = cities(OSMFILE)
print city


# In[3]:

#audit and cleaning for the sample osm file

OSMFILE = "p3plano_dallas_.osm"
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Dallas","Richardson","Street", "Avenue", "Boulevard", "Drive", "Place", "Square", "Road", 
            "Trail", "Parkway"]

# changing the variables in to new names
mapping = { "dallas":"Dallas",
            "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
             "Dr.": "Drive",
            "Blvd" : "Boulevard",
            "Dr" : "Drive",
            "W"  :"West",
           "Rd" : "Road",
            "way" :"Way"
            }


def audit_street_type(street_types, street_name): 
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    
    return street_types
pprint.pprint(dict(audit(OSMFILE)))

def update_name(name): # overabbrivating the street names
    update = []
    for splitting  in name.split(' '):
        if splitting in mapping.keys():
            splitting = mapping[splitting]
        update.append(splitting)
    return " ".join(update)


update_street = audit(OSMFILE) 

for street_type, ways in update_street.iteritems():
    for name in ways:
        new_name = update_name(name)
        cleaned = name, "=>", new_name  
        print name, "=>", new_name  

                
                
                
def phonenumber(OSMFILE):
    OSMFILE = open(OSMFILE,"r")
    phone_numbers =[]
    for event, elem in ET.iterparse(OSMFILE, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if(tag.attrib['k'] == "phone") or (tag.attrib['k'] == "contact:phone"):
                    phone_numbers.append(tag.attrib['v']) 
    return phone_numbers


def update_phonenumber(number):
    if re.compile(r'^(\d{3})(\d{3})(\d{4})$').search(number):
        return number[:3] + '-' + number[3:6] + '-' + number[6:]
    elif re.compile(r'^1(\d{10})$').search(number):
        return number[1:4] + '-' + number[4:7] + '-' + number[7:]
    elif re.compile(r'^\+1(\d{10})$').search(number):
        return number[2:5] + '-' + number[5:8] + '-' + number[8:]
    elif re.compile(r'^\+1\s(\d{10})$').search(number):
        return number[3:6] + '-' + number[6:9]  + '-' + number[9:]
    elif re.compile(r'^\+1\s(\d{3})\s(\d{3})(\d{4})$').search(number):
        return number[3:6] + '-' + number[7:10] + '-' + number[10:]
    elif re.compile(r'^01\s(\d{3})\s(\d{3})\s(\d{4})$').search(number):
        return number[3:].replace('','-')
    
    
    elif number.find(';') > 0:
        for i in number.split(';'):
            update_phonenumber(i) 
    
    
    elif len(re.findall('\d+',number)) >2:
        return '-'.join(re.findall('\d+',number))
    
    else:
        print number
        
def fix_phonenumbers(lists):
    for number in lists:
        fix_phonenumbers(number)

        
        
def validator(OSMFILE, schema):
    xmlschema_doc = ET.parse(schema)
    xmlschema = ET.XMLSchema(xmlschema_doc)
    for event, element in ET.iterparse(OSMFILE, events=("end", )):
        if not xmlschema.validate(element):
            print xmlschema.error_log
        
        




# In[5]:

# Thw phone numbers before cleaning the the data.
print phonenumber(OSMFILE)


# In[6]:

phone_numbers =  phonenumber(OSMFILE)#updated phone numbers for sample osm file
for phone_number in phone_numbers:
    print update_phonenumber(phone_number)

