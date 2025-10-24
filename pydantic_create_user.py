from pydantic import BaseModel, EmailStr, Field, constr


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias ='lastName')
    first_name: str = Field(alias ='firstName')
    middle_name: str = Field(alias ='middleName')

class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=128)
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserResponseSchema(BaseModel):
    user: UserSchema

