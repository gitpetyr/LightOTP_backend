import json,config

class DatabaseInit():
    def __init__(self):
        self.UserDBinit()
    class UserDBinit():
        def __init__(self):
            data={
                    "userinfo" : {
                        
                    }
                }
            with open(config.userdbConfig.userdb_path,"w") as userdb:
                json.dump(data,userdb)
if __name__ == "__main__":
    DatabaseInit()