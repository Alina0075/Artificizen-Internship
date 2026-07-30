from pydantic import BaseModel, EmailStr, field_validator
import re

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    @field_validator("email")
    @classmethod
    def validate_email(cls, email: EmailStr) -> EmailStr:
        email = str(email).strip()

        if " " in email:
            raise ValueError("Email must not contain spaces")

        return email
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if not re.fullmatch(
            r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}",
            password
        ):
            raise ValueError(
                "Password must be at least 8 characters and contain "
                "uppercase, lowercase, number, and special character"
            )

        return password

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = {
        "from_attributes": True}    