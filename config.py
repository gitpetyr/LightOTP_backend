import json

userdb_path="userdb.json"

class userdbConfig():
    def getdb(db):
        with open(userdb_path,"r") as f:
            return json.load(f)
        return "Fail"
    def writedb(db):
        with open(userdb_path,"w") as f:
            json.dump(db,f)
            return
        return