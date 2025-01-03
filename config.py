import json
import pyotp

userdb_path = "userdb.json"

def strcheck(s: str):
    if len(s) > 50:
        return False
    strset = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    for i in s:
        if i not in strset:
            return False
    return True

class userdbConfig:
    @staticmethod
    def initDb():
        try:
            with open(userdb_path, "r") as f:
                f.read()
                print("no error")
                pass
        except FileNotFoundError:
            print("has error")
            data = {
                "userinfo": {},
                "totpkeys": {}
            }
            userdbConfig.writeDb(data)

    @staticmethod
    def getDb():
        with open(userdb_path, "r") as f:
            data = json.load(f)
            if "totpkeys" not in data:
                data["totpkeys"] = {}
            return data

    @staticmethod
    def writeDb(db):
        with open(userdb_path, "w") as f:
            json.dump(db, f)

def getTOTPkey(key: str) -> str:
    return pyotp.TOTP(key).now()