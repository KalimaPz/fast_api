from typing import Optional
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str

app = FastAPI()
users = [
    {
        "id":1,
        "name" : "Donnukrit"
    },
     {
        "id":2,
        "name" : "John Doe"
    }
]
@app.get("/")
def root_page() :
    return "Hello World"

@app.get("/getAllUsers")
def getAllUsers() :
    return users

@app.post("/createUser")
async def createUser(user:User):
    last_idx = len(users)
    try : 
        if len(users) == 0 :
            users.append({
                "id" : 0,
                "name" : user.name 
            })
    
        else:
            users.append({
                "id" : last_idx + 1,
                "name" : user.name
            })
        return {
            "msg" : True,
            "data" : user
        }    
        
    except :
        print("error")
        return {
            "msg" : False,
        }
    
@app.get("/getUserById/{user_id}")
async def getUserById(user_id:int) :
    for user in users:
        if user["id"] == user_id:
            return {
                "msg" : True,
                "data" : user
            }
        else :
            return {
                "msg" : False,
                "data" : []
            }

    