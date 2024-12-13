import json,config

class DatabaseInit():
    def __init__(self):
        self.UserDBinit()
    class UserDBinit():
        def __init__(self):
            data={
                    "userinfo" : {
                        #(userid,usertoken)
                    }
                }
            config.userdbConfig.writedb(data)
if __name__ == "__main__":
    DatabaseInit()