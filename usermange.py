import config

class UserCheck():
    def add_userRecord(userid : str, usertoken : str):
        try:
            data=config.userdbConfig.getDb()
            if(userid in data["userinfo"]):
                return {"Fail" : "Userid already exists."}
            data["userinfo"][userid]={"token" : usertoken}
            print(data)
            config.userdbConfig.writeDb(data)
            return "Ok"
        except Exception as e:
            return {"Fail" : "Unknown error" , "debug" : str(e)}