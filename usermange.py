from hashlib import sha256
import config

class UserCheck():
    def add_userRecord(userid : str, usertoken : str):
        try:
            if not(config.strcheck(userid) and config.strcheck(usertoken)):
                return {
                        "Fail" : "The userid or usertoken does not match the requirements.",
                        "Debug": "The legal character set is qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
                    } 
            data=config.userdbConfig.getDb()
            if(userid in data["userinfo"]):
                return {"Fail" : "Userid already exists."}
            data["userinfo"][userid]={"token" : sha256(usertoken.encode("utf-8")).hexdigest()}
            # print(data)
            config.userdbConfig.writeDb(data)
            return "Ok"
        except Exception as e:
            return {"Fail" : "Unknown error." , "debug" : str(e)}
    def checkUserToken(userid : str, usertoken : str):
        try:
            data=config.userdbConfig.getDb()
            if not userid in data["userinfo"]:
                return {"Fail" : "The user does not exist."}
            print(sha256(usertoken.encode("utf-8")).hexdigest(),data["userinfo"][userid]["token"])
            if(sha256(usertoken.encode("utf-8")).hexdigest()==data["userinfo"][userid]["token"]):
                return {"Ok" : True}
            return {"Ok" : False}
        except Exception as e:
            return {"Fail" : "Unknown error." , "debug" : str(e)}