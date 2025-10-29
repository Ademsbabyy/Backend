# import jwt
# from dotenv import load_dotenv
# import os
# from datetime import datetime, timedelta
# from fastapi import Request
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from fastapi import Security



# bearer = HTTPBearer()

# load_dotenv()


# secret_key = os.getenv("secret_key")



# def create_token(details:dict, expiry:int):
#     expire = datetime.now() + timedelta(minutes = expiry)

#     details.update({"exp":expire})

#     encoded_jwt = jwt.encode(details, secret_key)

#     return encoded_jwt


# def verify_token(request: HTTPAuthorizationCredentials = Security(bearer)):
    
    
    
#     token = request.credentials


#     "Bearer 1iwiwi83iwuenje83839wjdj"


#     verified_token =  jwt.decode(token, secret_key, algorithms=["HS256"])

#     # expiry_time = verified_token.get("exp")







#     return {
#         "email": verified_token.get("email"),
#         "userType": verified_token.get("userType"),
#         "id" : verified_token.get("id")
#     }














import jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Security
bearer = HTTPBearer()
load_dotenv()
secret_key = os.getenv("secret_key")
def create_token(details: dict, expiry: int):
    expire = datetime.now() + timedelta(minutes=expiry)
    details.update({"exp": expire})
    encoded_jwt = jwt.encode(details, secret_key)
    return encoded_jwt
# def verify_token(request: Request):
#     payload = request.header.get("Authorization")
    #
#     token = payload.split(" ")[1]
#     verified_token = jwt.decode(token, secret_key, algorithms=["HS256"])
#     return {
#         "email": verified_token.get("email"),
#         "userType": verified_token.get("userType")
#     }
#  the down side of the approach above is the logged in will not be lock in our swagger documentation which is while we the using the approach bellow where by using
def verify_token(request: HTTPAuthorizationCredentials = Security(bearer)):
    token = request.credentials
    verified_token = jwt.decode(token, secret_key, algorithms=["HS256"])
    # expiry_time = verify_token.get("exp")
    return {
        "email": verified_token.get("email"),
        "userType": verified_token.get("userType"),
        "id": verified_token.get("id")
    }















