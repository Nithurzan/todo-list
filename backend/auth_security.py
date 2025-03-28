from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
import os



SECRET_KEY = os.getenv("SECRET_KEY", "mysecret")
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password,hashed_password):
    return pwd_context.verify(password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

def create_access_token(data:dict, expires_delta:timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta 
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM)



