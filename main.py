from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #allow all (for dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/name")
def getname():
    return {"name" : "Selva ganesh"}


@app.get("/age")
def getage():
    return {"age": "21"}

@app.get("/profession")
def getpro():
    return {"pro" : "doing everything for youuuu"}

@app.get("/love")
def getlove():
    return {"love" : "It's you 🫵 💖"}

@app.get("/who")
def getangel():
    return {"who" : "It's you my bibuuu 😘🥰💖🥰😍🥰"}