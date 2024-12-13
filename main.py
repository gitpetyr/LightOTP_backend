from fastapi import FastAPI
import usermange

app = FastAPI()

@app.get("/")
def read_root():
    return "LightOTP API"

@app.get("/register")
def register_route(userid : str, usertoken : str):
    return {
            "res" : usermange.UserCheck.register() , 
            "requests" : {
                "userid" : userid,
                "usertoken" : usertoken
            }
        }