from hashlib import sha256
import config
import AES

class UserCheck:
    @staticmethod
    def add_userRecord(userid: str, usertoken: str):
        config.userdbConfig.initDb()  # 初始化数据库
        if not (config.strcheck(userid) and config.strcheck(usertoken)):
            return {
                "Fail": "The userid or usertoken does not match the requirements.",
                "Debug": "The legal character set is qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
            }
        data = config.userdbConfig.getDb()
        if userid in data["userinfo"]:
            return {"Fail": "Userid already exists."}
        data["userinfo"][userid] = {"token": sha256(usertoken.encode("utf-8")).hexdigest()}
        config.userdbConfig.writeDb(data)
        return "Ok"

    @staticmethod
    def checkUserToken(userid: str, usertoken: str):
        config.userdbConfig.initDb()  # 初始化数据库
        data = config.userdbConfig.getDb()
        if userid not in data["userinfo"]:
            return {"Fail": "The user does not exist."}
        if sha256(usertoken.encode("utf-8")).hexdigest() == data["userinfo"][userid]["token"]:
            return {"Ok": True}
        return {"Ok": False}

    @staticmethod
    def add_totp(userid: str, usertoken: str, totpname: str, totpkey: str):
        config.userdbConfig.initDb()  # 初始化数据库
        if not (config.strcheck(userid) and config.strcheck(usertoken) and config.strcheck(totpname) and config.strcheck(totpkey)):
            return {
                "Fail": "The userid, usertoken, totpname, or totpkey does not match the requirements.",
                "Debug": "The legal character set is qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
            }
        data = config.userdbConfig.getDb()
        if userid not in data["userinfo"]:
            return {"Fail": "The user does not exist."}
        if sha256(usertoken.encode("utf-8")).hexdigest() != data["userinfo"][userid]["token"]:
            return {"Fail": "Invalid token."}
        if "totpkeys" not in data:
            data["totpkeys"] = {}
        if userid not in data["totpkeys"]:
            data["totpkeys"][userid] = {}
        if totpname in data["totpkeys"][userid]:
            return {"Fail": "TOTP name already exists."}
        
        encrypted_totpkey = AES.encrypt(usertoken, totpkey)
        
        data["totpkeys"][userid][totpname] = encrypted_totpkey
        config.userdbConfig.writeDb(data)
        return "Ok"

    @staticmethod
    def get_totp(userid: str, usertoken: str, totpname: str):
        config.userdbConfig.initDb()  # 初始化数据库
        data = config.userdbConfig.getDb()
        if userid not in data["userinfo"]:
            return {"Fail": "The user does not exist."}
        if sha256(usertoken.encode("utf-8")).hexdigest() != data["userinfo"][userid]["token"]:
            return {"Fail": "Invalid token."}
        if userid not in data["totpkeys"] or totpname not in data["totpkeys"][userid]:
            return {"Fail": "TOTP name does not exist."}
        
        encrypted_totpkey = data["totpkeys"][userid][totpname]
        decrypted_totpkey = AES.decrypt(usertoken, encrypted_totpkey)
        
        return {"totpkey": config.getTOTPkey(decrypted_totpkey)}

    @staticmethod
    def get_totplist(userid: str, usertoken: str):
        config.userdbConfig.initDb()  # 初始化数据库
        data = config.userdbConfig.getDb()
        if userid not in data["userinfo"]:
            return {"Fail": "The user does not exist."}
        if sha256(usertoken.encode("utf-8")).hexdigest() != data["userinfo"][userid]["token"]:
            return {"Fail": "Invalid token."}
        if userid not in data["totpkeys"]:
            return {"Fail": "No TOTP keys found for the user."}
        
        totpnames = list(data["totpkeys"][userid].keys())
        return {"totpnames": totpnames}

    @staticmethod
    def del_totp(userid: str, usertoken: str, totpname: str):
        config.userdbConfig.initDb()  # 初始化数据库
        data = config.userdbConfig.getDb()
        if userid not in data["userinfo"]:
            return {"Fail": "The user does not exist."}
        if sha256(usertoken.encode("utf-8")).hexdigest() != data["userinfo"][userid]["token"]:
            return {"Fail": "Invalid token."}
        if userid not in data["totpkeys"] or totpname not in data["totpkeys"][userid]:
            return {"Fail": "TOTP name does not exist."}
        
        del data["totpkeys"][userid][totpname]
        config.userdbConfig.writeDb(data)
        return "Ok"