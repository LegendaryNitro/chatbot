import requests
import sys
from base64 import b64decode
sys.path.append('../')
sys.path.append('../imports')
from fastapi import FastAPI, Body, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import uvicorn

from main import CustomCrew

app = FastAPI()
triggered_endpoints = set()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3006"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"]
)

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail="Error forwarding request: " + str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))
    return wrapper


## CALLING THE CREWS
@app.post("/custom-question")
async def custom_crew(question = Body(...)):
    custom_crew = CustomCrew(question)
    hero = custom_crew.run()
    print(hero)

    return JSONResponse(content={"message": "Requests triggered successfully", "answer":hero}, media_type="application/json")



