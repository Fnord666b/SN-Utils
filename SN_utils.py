import urllib.parse
import urllib.request
import json

# Story related requests

def get_story_reskey():

    url="https://dev.soylentnews.org/api.pl?m=story&op=reskey"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
    resp = json.loads(the_page);
    res_key = resp["reskey"]
    return(res_key)

# Comment related requests

def get_comment_reskey():

    url="https://dev.soylentnews.org/api.pl?m=comment&op=reskey"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
    resp = json.loads(the_page);
    res_key = resp["reskey"]
    return(res_key)

def get_comment_by_cid(cid):

    url="https://soylentnews.org/api.pl?m=comment&op=single&cid=" + str(cid)
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
    resp = json.loads(the_page);    
    return(resp)
    
#  User related requests

def get_maxuid():

    url="https://dev.soylentnews.org/api.pl?m=user&op=max_uid"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
    resp = json.loads(the_page);
    max_uid = resp["max_uid"]
    return(max_uid)

def get_uid(nickname):
    
    url="https://soylentnews.org/api.pl?m=user&op=get_uid&nick=" 
    url = url + urllib.parse.quote_plus(nickname)
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
    resp = json.loads(the_page);    
    uid = resp["uid"]
    return(uid)
    
def get_nick(uid):
    
    url="https://soylentnews.org/api.pl?m=user&op=get_nick&uid=" + str(uid)
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
    resp = json.loads(the_page);    
    nick = resp["nick"]
    return(nick)
    
def get_user(uid):
    
    url="https://soylentnews.org/api.pl?m=user&op=get_user&uid=" + str(uid)
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
    user = json.loads(the_page);    
    return(user)