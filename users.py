# from database import db
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from sqlalchemy import text
# import os
# import bcrypt
# import uvicorn
# from dotenv import load_dotenv



# load_dotenv()


# app = FastAPI(title = "Simple App", version = "1.0.0")

# class Simple(BaseModel):
#     name: str = Field(..., example = "Sam Larry")
#     email: str = Field(..., example = "sam@gmail.com")
#     password: str = Field(..., example = "sam123")



# # @app.post("/signup")
# # def signUp(input: Simple):

# #     try:
# #         query = text("""
# #             INSERT INTO users (name, email, password)
# #              VALUES (:name, :email, :password)        #placeholder
# # """)
        
# #         hashedPassword = bcrypt.hashpw(input.password)

# #         db.execute(query, {"name": input.name, "email": input.email, "password":input.password})

# #         db.commit()

# #         return {"message":"User created successfully", "data":{"name":input.name, "email": input.email}}

# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail = e)












# # @app.post("/signup")
# # def signup(input:Simple):
# #     try:



# #         duplicate_query = text("""
# #                 SELECT * FROM users
# #                 WHERE email = :email
# #                         """)
        
# #         existing=db.execute(duplicate_query, {"email":input.email})

# #         if existing:
# #             print("aa")
# #             # raise HTTPException(status_code=400, detail="Email already exists")













# #         query= text(""" INSERT INTO users (name,email,password)
# #                            VALUES (:name,:email, :password)
# #         """)
# #         salt=bcrypt.gensalt()
# #         hashedpassword =bcrypt.hashpw(input.password.encode('utf-8'), salt)
# #         print(hashedpassword)
# #         db.execute(query, {'name':input.name, 'email': input.email, 'password': hashedpassword})
# #         db.commit()


# #         return{"message":"User created successfully",
# #                "data":{"name":input.name, "email":input.email}}



# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail = e)
    



    
# # if __name__=="__main__":
# #     uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))















# @app.post("/signup")
# def signup(input: Simple):
#     try:
#         # Check if email already exists
#         duplicate_query = text("""
#             SELECT * FROM users WHERE email = :email
#         """)
#         existing = db.execute(duplicate_query, {"email": input.email}).fetchone()

#         if existing:
#             raise HTTPException(status_code=400, detail="Email already exists")

#         # Hash the password
#         salt = bcrypt.gensalt()
#         hashed_password = bcrypt.hashpw(input.password.encode('utf-8'), salt)

#         # Insert user into DB
#         insert_query = text("""
#             INSERT INTO users (name, email, password)
#             VALUES (:name, :email, :password)
#         """)
#         db.execute(insert_query, {
#             "name": input.name,
#             "email": input.email,
#             "password": hashed_password.decode('utf-8')  # Store as string
#         })

#         db.commit()

#         return {
#             "message": "User created successfully",
#             "data": {
#                 "name": input.name,
#                 "email": input.email
#             }
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))






















from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import bcrypt
import uvicorn
import jwt
load_dotenv()











app = FastAPI(title="Simple App", version="1.0.0")
class Simple(BaseModel):
    name: str = Field(..., example="Sam Larry")
    email: str = Field(..., example="sam@email.com")
    password: str = Field(..., example="sam123")
    userType: str = Field(...,example = "student")




@app.post("/signup")
def signUp(input: Simple):
    try:
        duplicate_query=text("""
            SELECT * FROM users
            WHERE email = :email
                             """)
        existing = db.execute(duplicate_query, {"email": input.email})
        if existing:
            print("Email already exists")
            # raise HTTPException(status_code=400, detail="Email already exists")
        query = text("""
            INSERT INTO users (name, email, password,userType)
            VALUES (:name, :email, :password, :userType)
        """)
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)
        print(hashedPassword)
        db.execute(query, {"name": input.name, "email": input.email, "password": hashedPassword,"userType": input.userType})
        db.commit()
        return {"message": "User created successfully",
                "data": {"name": input.name, "email": input.email,"usertype":input.userType}}
    except Exception as e:
        raise HTTPException(status_code=500, detail = e)
    











# Building a login endpoint

class LoginRequest(BaseModel):
    email: str = Field(...,example = "sam@gmail.com")
    password: str = Field(..., example = "sam123")
   




@app.post("/login")
def login(input:LoginRequest):
    try:
        query = text("""
            SELECT * FROM users WHERE email = :email


            """)
        result  = db.execute(query,{"email":input.email} ).fetchone()


        if not result:
            raise HTTPException(status_code=404, detail = "Invalid email or password")
        

        verified_password = bcrypt.checkpw(input.password.encode('utf-8'), result.password.encode('utf-8'))

        if not verified_password:
             raise HTTPException(status_code=404, detail = "Invalid email or password")
        
        return {
            "message":"Login Successful"
        }






    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))

























if __name__=="__main__":
    uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))





