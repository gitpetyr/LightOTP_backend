import json
class userdbConfig():
    userdb_path="userdb.json"
    def getdb(self):
        with open(self.userdb_path,"r") as f:
            return json.load(f)