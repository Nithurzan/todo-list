from fastapi import FastAPI
from routes import auth,todo
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(todo.router, prefix="/todos", tags=["ToDos"])


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI To-Do List"}