from typing import Optional
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    faculty : str
    dept : str
    
app = FastAPI()
users = [
    {
        "id":1,
        "name" : "Donnukrit",
        "faculty" : "Engineering",
        "dept" : "Computer Engineering"
    },
     
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
                "name" : user.name ,
                "faculty" : user.faculty,
                "dept": user.dept
            })
    
        else:
            users.append({
                "id" : last_idx + 1,
                "name" : user.name ,
                "faculty" : user.faculty,
                "dept": user.dept
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
    try:
        for user in users:
            if user_id is user["id"]:
                return {
                    "msg" : True,
                    "data" : user
                }
        return {
            "msg" : False,
            "data" : "User does not exist."
        }
            
    except: 
        return {
            "msg" : False,
            "data" : "exception occured."
    }

@app.delete("/deleteUser/{user_id}")
async def deleteUserById(user_id:int):
    for user in users:
        if user_id == user["id"]:
            print(user)
            remove_index = users.index(user)
            users.pop(remove_index)
            return {
                "msg":True,
                "data" : "User has been delete"
            }
        else: 
            return {
                "msg":False,
                "data" : "User does not exist."
            }
            
            
    
            