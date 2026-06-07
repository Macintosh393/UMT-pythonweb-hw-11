from pydantic import BaseModel, Field, EmailStr, ConfigDict

class UserResponse(BaseModel):
    id: int
    username: str = Field(min_length=2, max_length=100)
    email: EmailStr
    avatar: str

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    username: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=6, max_length=50)
