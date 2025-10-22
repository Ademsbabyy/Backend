from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import bcrypt
import uvicorn

load_dotenv()
app = FastAPI(title="Simple API App", version="1.0.0")
class Users(BaseModel):
    name: str = Field(..., example="Jay jay")
    email: str = Field(..., example="jsjjsy@publica.io")
    password: str = Field(..., example="@gfjeoi")

@app.post("/signup")
def signUp(input: Users):
    try:
        duplicate_query = text("""
              SELECT * FROM users
              WHERE email = :email
                              """)
        existing = db.execute(duplicate_query, {"email": input.email})
        if existing:
            print("Email already exist")
            # raise HTTPException(status_code=400, detail="Email already exists")
        query = text("""
            INSERT INTO users (name, email, password)
            VALUES (:name, :email, :password)
        """)
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(input.password.encode("utf-8"), salt)
        print(hashedPassword)
        db.execute(query, {"name": input.name,
                   "email": input.email, "password": hashedPassword})
        db.commit()
        return {"message": "user created successfully",
                "data": {"name": input.name, "email": input.email}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))














