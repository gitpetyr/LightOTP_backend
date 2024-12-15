import json

userdb_path="userdb.json"

def strcheck(s : str):
    if len(s)>50:
        return False
    strset="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    for i in s:
        if not i in strset:
            return False
    return True

class userdbConfig():
    def getDb():
        with open(userdb_path,"r") as f:
            return json.load(f)
        return "Fail"
    def writeDb(db):
        with open(userdb_path,"w") as f:
            json.dump(db,f)
            return
        return