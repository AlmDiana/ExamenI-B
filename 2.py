#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "EPdpilWg2fgrJPUFlr3CxFIca"
csecret = "6j7FbS7bRixnU962iLDEXAxOuLPF4Ub2fegqH2pXkboKJbfGnD"
atoken = "1415810816264347658-SvqxMszZ41wAEoj1mzcFF6nszkH3o1"
asecret = "7cGFpnexPc88nFY9pc7udPqnV87xSjnZvKBkzjaKe57Ef"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://AlmDiana:d17121998k@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('juegosolimpicos')
except:
    db = server['juegosolimpicos']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[139.661588,35.641458,139.723927,35.692142])  
twitterStream.filter(track=['juegosolimpicos','olimpiadas2021', 'juegos2021','Tokioolimpiadas'])


# In[ ]:




