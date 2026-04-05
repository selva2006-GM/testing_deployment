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
    return {"age": "19"}

@app.get("/profession")
def getpro():
    return {"pro" : "doing everything for youuuu"}

@app.get("/love")
def getlove():
    return {"love" : "It's you 🫵 💖"}

@app.get("/who")
def getangel():
    return {"who" : "It's you my bibuuu 😘🥰💖🥰😍🥰"}

@app.get("/favorite")
def getfav():
    return {"favorite" : "my moms warm and + now your presence in my life"}

@app.get("/wish")
def getwish():
    return {"wish" :'''one day me you my both papas and mummys all ayu,
            mukitha , kingu or kingi sitting together gossiping about our neighbours 🤣
            and watching kingus play and enjoying everyone and i will protect everyone i love my family'''}

@app.get("/dream")

def getdream():
    return{"dream" : '''show everyone , an example of love , and my small family with each
           day a happiest day for all no tension just joy'''}
