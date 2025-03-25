from fastapi import APIRouter,HTTPException
from schema import SignupRequest,LoginRequest
from auth_security import hash_password,verify_password,create_access_token
from database import users_collection



router = APIRouter()

async def get_user(username: str):
    user = await users_collection.find_one({"username": username})
    return user


@router.post("/signup")
async def signup(request: SignupRequest):
    existing_user = await get_user(request.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = hash_password(request.password)
    user_data = {"username": request.username, "password": hashed_password}
    await users_collection.insert_one(user_data)
    return {"success":True, "message": "User created"}

@router.post("/login")
async def login(request: LoginRequest):
    user = await get_user(request.username)
    if not user or not verify_password(request.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token({"sub": user["username"]})
    return {"success": True, "message":"Login succesfull", "access_token": token}