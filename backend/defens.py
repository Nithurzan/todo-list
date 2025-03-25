from fastapi import HTTPException, Depends
import jwt


def get_current_user(token:str):
    try:
        payload = jwt.decode(token, "mysecret", algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    
    