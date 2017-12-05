
# coding: utf-8

# ## Please dont alter the order.

# In[4]:

import csv, sqlite3


load = sqlite3.connect("p3plano_dallas_.db")

load.text_factory = str

clf = load.cursor()


# In[5]:

sqlite_file = "p3plano_dallas_.db"
load = sqlite3.connect(sqlite_file)
clf = load.cursor()


# In[65]:

clf.execute('DROP TABLE IF EXISTS new_node_table')
load.commit()


# In[66]:

#nodes table
clf.execute("CREATE TABLE new_node_table (id, lat, lon, user, uid, version, changeset, timestamp);")

with open('nodes.csv','rb') as ii:

    directory = csv.DictReader(ii) 

    todatabase = [(i['id'], i['lat'], i['lon'], i['user'].decode("utf-8"),  i['uid'], i['version'], i['changeset'], i['timestamp'])              for i in directory]

clf.executemany("INSERT INTO new_node_table (id, lat, lon, user, uid, version, changeset, timestamp)                VALUES (?, ?, ?,?, ?, ?, ?, ?);", todatabase)

load.commit()



# In[5]:

def new_node_table():
    result = clf.execute('SELECT COUNT(*) FROM new_node_table')
    resultsList = list(result)[0][0]
    return resultsList

print "no.of nodes:", new_node_table()


# In[6]:

def new_node_table():
    result = clf.execute('SELECT * FROM new_node_table')
    resultsList = list(result)[0][0]
    return resultsList

print "no.of nodes:", new_node_table()


# In[7]:

clf.execute('DROP TABLE IF EXISTS new_nodes_tagss')
load.commit()


# In[8]:

#load.text_factory = str
clf.execute("CREATE TABLE new_nodes_tagss (id, key, value, type);")

with open('nodes_tags.csv','rb') as ii:
    directory = csv.DictReader(ii) 
    todatabase = [(i['id'], i['key'], i['value'].decode("utf-8"), i['type'] )              for i in directory]
clf.executemany("INSERT INTO new_nodes_tagss (id, key, value, type) VALUES (?, ?, ?, ?);", todatabase)
load.commit()


# In[9]:

def new_nodes_tagss():
    result = clf.execute('SELECT COUNT(*) FROM new_nodes_tagss')
    resultsList = list(result)[0][0]
    return resultsList

print "no.of node_tags:", new_nodes_tagss()


# In[10]:

clf.execute('DROP TABLE IF EXISTS new_wayss')
load.commit()


# In[11]:

## ways table

clf.execute("CREATE TABLE new_wayss (id, user, uid, version, changeset, timestamp);")
with open('ways.csv','rb') as jj:
    directory = csv.DictReader(jj) 
    todatabase = [(i['id'], i['user'].decode("utf-8"),  i['uid'], i['version'], i['changeset'], i['timestamp']) for i in directory]


clf.executemany("INSERT INTO new_wayss (id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", todatabase)

load.commit()


# In[12]:

def new_wayss():
    result = clf.execute('SELECT COUNT(*) FROM new_wayss')
    resultsList = list(result)[0][0]
    return resultsList

print "no.of ways:", new_wayss()


# In[13]:

clf.execute('DROP TABLE IF EXISTS new_ways_node')
load.commit()


# In[14]:

##ways_nodes table

clf.execute("CREATE TABLE new_ways_node (id, node_id, position);")
with open('ways_nodes.csv','rb') as jj:
    directory = csv.DictReader(jj) 
    todatabase = [(i['id'], i['node_id'], i['position']) for i in directory]
clf.executemany("INSERT INTO new_ways_node (id, node_id, position) VALUES (?, ?, ?);", todatabase)
load.commit()


# In[15]:

def new_ways_node():
    result = clf.execute('SELECT COUNT(*) FROM new_ways_node')
    resultsList = list(result)[0][0]
    return resultsList

print "no.of ways_node:", new_ways_node()


# In[16]:

clf.execute('DROP TABLE IF EXISTS new_way_tags')
load.commit()


# In[17]:

#ways_tags table

clf.execute("CREATE TABLE new_way_tags (id, key, value, type);")
with open('ways_tags.csv','rb') as k:
    directory = csv.DictReader(k) 
    todatabse = ((i['id'], i['key'], i['value'].decode["utf-8"], i['type']) for i in directory)

#clf.executemany("INSERT INTO new_way_tags id, key, value, type) VALUES (?, ?, ?, ?);", todatabase)
load.commit()


# In[18]:

def ways_tags():
    result = clf.execute('SELECT COUNT(*) FROM ways_tags')
    resultsList = list(result)[0][0]
    return resultsList

print "no.of ways_tags:", ways_tags()
print "done"


# In[19]:

r = clf.execute('SELECT COUNT(*) FROM new_nodes_tagss')
print list(r )


# In[20]:

r = clf.execute('SELECT COUNT(*) FROM new_node_table')
print list(r )


# In[21]:

r = clf.execute('SELECT * FROM new_nodes_tagss')
print list(r )


# In[70]:

def street():
    r = clf.execute('''SELECT tags.value, COUNT(*) as count FROM (SELECT * FROM new_nodes_tagss UNION ALL 
                                                                        SELECT * FROM ways_tags) tags
                                                                        WHERE tags.key='street'
                                                                        GROUP BY tags.value
                                                                        ORDER BY count DESC LIMIT 20;''')
    return list(r)
ResultChild = street()

print "there list"


from pprint import pprint
pprint(ResultChild)


# In[72]:

def phone():
    r = clf.execute('''SELECT tags.value, COUNT(*) as count FROM (SELECT * FROM new_nodes_tagss UNION ALL 
                                                                        SELECT * FROM ways_tags) tags
                                                                        WHERE tags.key='phone'
                                                                        GROUP BY tags.value
                                                                        ORDER BY count DESC LIMIT 10;''')
    return list(r)
ResultChild = phone()


print "there list"

from pprint import pprint
pprint(ResultChild)


# In[77]:

def cities():
    r = clf.execute('''SELECT tags.value, COUNT(*) as count FROM (SELECT * FROM new_nodes_tagss UNION ALL 
                                                                SELECT * FROM ways_tags) tags
                                                                WHERE tags.key LIKE '%city'
                                                                GROUP BY tags.value
                                                                ORDER BY count DESC;''')
    return list(r)
ResultChild = cities()

print "there list"


from pprint import pprint
pprint(ResultChild)


# In[101]:

def unique_users():
    r = clf.execute('''SELECT COUNT(DISTINCT(i.uid))FROM (SELECT uid FROM new_node_table UNION ALL SELECT uid FROM new_wayss) i;''')
    return list(r)
ResultChild = unique_users()



from pprint import pprint
pprint(ResultChild)


# In[104]:

def top_users():
    r = clf.execute('''SELECT i.user, COUNT(*) as num
                        FROM (SELECT user FROM new_node_table UNION ALL SELECT user FROM new_wayss) i
                        GROUP BY i.user
                        ORDER BY num DESC
                        LIMIT 5;''')
    return list(r)
ResultChild = top_users()

print "there list"


from pprint import pprint
pprint(ResultChild)


# In[103]:

def onetime_users():
    r = clf.execute('''SELECT COUNT(*) FROM (SELECT i.user, COUNT(*) as num FROM 
                        (SELECT user FROM new_node_table UNION ALL SELECT user FROM new_wayss) i
                        GROUP BY i.user HAVING num=1)  u;''')
    return list(r)
ResultChild = onetime_users()



from pprint import pprint
pprint(ResultChild)


# In[83]:

def postcodes():
        r = clf.execute('''SELECT tags.value, COUNT(*) as count FROM (SELECT * FROM new_nodes_tagss UNION ALL 
                                                                    SELECT * FROM ways_tags) tags
                                                                    WHERE tags.key LIKE '%postcode'
                                                                    GROUP BY tags.value
                                                                    ORDER BY count DESC;''')
    return list(r)
ResultChild = postcodes()

print "there list"


from pprint import pprint
pprint(ResultChild)


# In[107]:

def top_amenties():
    r = clf.execute('''SELECT value, COUNT(*) as num FROM new_nodes_tagss WHERE key='amenity' GROUP BY value
                                     ORDER BY num DESC LIMIT 20;''')
    return list(r)
ResultChild = top_amenties()

print "there list"


from pprint import pprint
pprint(ResultChild)


# In[91]:

def popular_religion():
    r = clf.execute('''SELECT new_nodes_tagss.value, COUNT(*) as num FROM new_nodes_tagss JOIN 
                           (SELECT DISTINCT(id) FROM new_nodes_tagss
                             WHERE value='place_of_worship') i
                            ON new_nodes_tagss.id=i.id WHERE new_nodes_tagss.key='religion' 
                            GROUP BY new_nodes_tagss.value
                           ORDER BY num DESC LIMIT 2;''')
    return list(r)
ResultChild = popular_religion()

print "there list"


from pprint import pprint
pprint(ResultChild)


# In[109]:

def popular_cuisines():
    r = clf.execute('''SELECT new_nodes_tagss.value, COUNT(*) as num FROM new_nodes_tagss 
                       JOIN (SELECT DISTINCT(id) FROM new_nodes_tagss WHERE value='restaurant') i
                      ON new_nodes_tagss.id=i.id WHERE new_nodes_tagss.key='cuisine'
                      GROUP BY new_nodes_tagss.value ORDER BY num DESC;''')
    return list(r)
cuisines = popular_cuisines()



from pprint import pprint
pprint(cuisines)


# In[32]:

def highway_child():
    r = clf.execute('''SELECT * 
                       FROM new_nodes_tagss
                       JOIN (SELECT DISTINCT(id) FROM new_nodes_tagss WHERE value="traffic_signals") i 
                       ON new_nodes_tagss.id=i.id;''')
    return list(r)
ResultChild = highway_child()
print len(ResultChild)
pprint(ResultChild)


# In[156]:

#the resturants well known in our city

def cuisines():
    for i in clf.execute('SELECT ways_tags.value, COUNT(*) as num                             FROM ways_tags                             JOIN (SELECT DISTINCT(id) FROM ways_tags WHERE value="restaurant") i                             ON ways_tags.id=i.id                             WHERE ways_tags.key="cuisine"                             GROUP BY ways_tags.value                             ORDER BY num DESC'):
        return i



print cuisines()


# In[64]:

def popular_cuisines():
    r = clf.execute('''SELECT *
                             FROM ways_tags
                             JOIN (SELECT DISTINCT(id) FROM ways_tags WHERE key="cuisine") i 
                             ON ways_tags.id=i.id;''')
    return list(r)

cusineresult = popular_cuisines()
print len(cusineresult)

print "there list"

from pprint import pprint
pprint(cusineresult)


# In[171]:

#Ammenties in our selected data
def ammenties():        
    r = clf.execute('''SELECT * 
                             FROM ways_tags
                             JOIN (SELECT DISTINCT(id) FROM ways_tags WHERE key="amenity") i 
                             ON ways_tags.id=i.id;''')
    return list(r)


# In[172]:

amenty_result= ammentiess()
print len(amenty_result)

print "there list"

from pprint import pprint
pprint(amenty_result)


# In[55]:

def religion():     ##the places of worship of god 
    r = clf.execute('''SELECT * 
                             FROM ways_tags
                             JOIN (SELECT DISTINCT(id) FROM ways_tags WHERE key="religion") i 
                             ON ways_tags.id=i.id;''')
    return list(r)


# In[56]:

religionresult = religion()
print len(religionresult)

print "there list"

from pprint import pprint
pprint(religionresult)


# In[ ]:




# In[ ]:




# In[24]:

def highway_child():
    results = clf.execute('''SELECT * 
                             FROM new_nodes_tagss
                             JOIN (SELECT DISTINCT(id) FROM new_nodes_tagss WHERE key="highway") i 
                             ON new_nodes_tagss.id=i.id;''')
    return list(results)
restResultChildren = highway_child()
print len(restResultChildren)
pprint(restResultChildren)


# In[23]:

def highways():
    names = clf.execute('''SELECT new_nodes_tagss.value, COUNT(*) as num
    FROM new_nodes_tagss
    JOIN(SELECT DISTINCT (id) FROM new_nodes_tagss WHERE key = 'highway') as i
    ON new_nodes_tagss.id = i.id
    WHERE new_nodes_tagss.key ='highway' 
    GROUP BY new_nodes_tagss.value
    ORDER BY num DESC;''')
    return list(names)

print highways()


# In[26]:

def traffic_signal():
    r = clf.execute('''SELECT count(*) FROM new_nodes_tagss WHERE value ='traffic_signals';''')
    return list(r)
Results = traffic_signal()
print len(Results)
from pprint import pprint
pprint(Results)


# In[22]:

def highway():
    results = clf.execute('''SELECT count(*) FROM new_nodes_tagss WHERE key='highway';''')
    return list(results)
restResults = highway()
print len(restResults)
from pprint import pprint
pprint(restResults)

