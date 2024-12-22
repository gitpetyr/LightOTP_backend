from fastapi import FastAPI
import usermange

app = FastAPI()

@app.get("/")
def read_root():
    return "LightOTP API"

@app.get("/register")
def register_route(userid: str, usertoken: str):
    try:
        return {
            "res": usermange.UserCheck.add_userRecord(userid, usertoken),
            "requests": {
                "userid": userid,
                "usertoken": usertoken
            }
        }
    except Exception as e:
        return {"Fail": "Unknown error.", "debug": str(e)}

@app.get("/test/checktoken")
def checkusertoken(userid: str, usertoken: str):
    try:
        return {
            "res": usermange.UserCheck.checkUserToken(userid, usertoken),
            "requests": {
                "userid": userid,
                "usertoken": usertoken
            }
        }
    except Exception as e:
        return {"Fail": "Unknown error.", "debug": str(e)}

@app.get("/addtotp")
def add_totp(userid: str, usertoken: str, totpname: str, totpkey: str):
    try:
        return {
            "res": usermange.UserCheck.add_totp(userid, usertoken, totpname, totpkey),
            "requests": {
                "userid": userid,
                "usertoken": usertoken,
                "totpname": totpname,
                "totpkey": totpkey
            }
        }
    except Exception as e:
        return {"Fail": "Unknown error.", "debug": str(e)}

@app.get("/gettotp")
def get_totp(userid: str, usertoken: str, totpname: str):
    try:
        return {
            "res": usermange.UserCheck.get_totp(userid, usertoken, totpname),
            "requests": {
                "userid": userid,
                "usertoken": usertoken,
                "totpname": totpname
            }
        }
    except Exception as e:
        return {"Fail": "Unknown error.", "debug": str(e)}

@app.get("/gettotplist")
def get_totplist(userid: str, usertoken: str):
    try:
        return {
            "res": usermange.UserCheck.get_totplist(userid, usertoken),
            "requests": {
                "userid": userid,
                "usertoken": usertoken
            }
        }
    except Exception as e:
        return {"Fail": "Unknown error.", "debug": str(e)}