from fastapi import FastAPI
import usermange

app = FastAPI()

@app.get("/")
def read_root():
    return "LightOTP API"

@app.get("/register")
def register_route(userid : str, usertoken : str):
    return {
            "res" : usermange.UserCheck.add_userRecord(userid,usertoken), 
            "requests" : {
                "userid" : userid,
                "usertoken" : usertoken
            }
        }

@app.get("/test/checktoken")
def checkusertoken(userid : str,usertoken :str):
    return {
            "res" : usermange.UserCheck.checkUserToken(userid,usertoken),
            "requests" : {
                "userid" : userid,
                "usertoken" : usertoken
            }
        }