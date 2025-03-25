from model import ToDo,User

class ToDoDB(ToDo):
    id : str

    class Config:
        orm_mode = True



class SignupRequest(User):
    pass

class LoginRequest(User):
    pass