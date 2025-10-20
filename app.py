from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

app = FastAPI(title = "Simple FastAPI App", version = "1.0.0")

@app.get("/")
def root():
    return "Message : ""Welcome to my fastAPI Application"


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port = int(os.getenv("port")))