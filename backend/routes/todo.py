import logging
from bson import ObjectId
from fastapi import APIRouter,HTTPException,Depends
from model import ToDo
from database import todos_collection
from database import db
from defens import get_current_user


router = APIRouter()

def convert_objectid_to_str(data):
    """Recursively convert ObjectId to string."""
    if isinstance(data, ObjectId):
        return str(data)
    if isinstance(data, dict):
        return {key: convert_objectid_to_str(value) for key, value in data.items()}
    if isinstance(data, list):
        return [convert_objectid_to_str(item) for item in data]
    return data


@router.post("/")
async def create_todo(todo:ToDo, user: str = Depends(get_current_user)):
    todo_data = todo.dict()
    todo_data["user"] = user
    result = await todos_collection.insert_one(todo_data)
    created_todo = {**todo_data, "id": str(result.inserted_id)}
    return convert_objectid_to_str(created_todo)


@router.get("/")
async def get_todos(user: str = Depends(get_current_user)):
    todos = await todos_collection.find({"user": user}).to_list(100)
    return [convert_objectid_to_str(todo) for todo in todos]



@router.get("/completed")
async def get_completed_todos(user: str = Depends(get_current_user)):
    todos = await todos_collection.find({"user": user, "completed": True}).to_list(100)
    return [convert_objectid_to_str(todo) for todo in todos]



@router.put("/{todo_id}")
async def update_todo(todo_id:str, todo:ToDo, user: str = Depends(get_current_user)):
    try:
        todo_id_obj = ObjectId(todo_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid todo_id format")
    logging.info(f"Updating ToDo with ID: {todo_id_obj} and User: {user}")
    
    result = await todos_collection.update_one(
        {"_id": ObjectId(todo_id), "user": user},
        {"$set": todo.dict()}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="To-Do not found")
    updated_todo = await todos_collection.find_one({"_id": todo_id_obj})
    
    return convert_objectid_to_str(updated_todo)




@router.put("/{todo_id}/complete")
async def mark_todo_completed(todo_id: str, user: str = Depends(get_current_user)):
    await todos_collection.update_one(
        {"_id": ObjectId(todo_id), "user": user},
        {"$set": {"completed": True}}
    )
    updated_todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})
    return convert_objectid_to_str(updated_todo)



@router.put("/{todo_id}/uncomplete")
async def mark_todo_completed(todo_id: str, user: str = Depends(get_current_user)):
    await todos_collection.update_one(
        {"_id": ObjectId(todo_id), "user": user},
        {"$set": {"completed": False}}
    )
    updated_todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})
    return convert_objectid_to_str(updated_todo)


@router.delete("/{todo_id}")
async def delete_todo(todo_id: str, user: str = Depends(get_current_user)):
    await todos_collection.delete_one({"_id": ObjectId(todo_id), "user": user})
    return {"message": "To-Do deleted"}
 