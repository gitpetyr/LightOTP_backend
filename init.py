import config

class DatabaseInit:
    def __init__(self):
        self.UserDBinit()

    class UserDBinit:
        def __init__(self):
            data = {
                "userinfo": {}
            }
            config.userdbConfig.writeDb(data)

if __name__ == "__main__":
    DatabaseInit()