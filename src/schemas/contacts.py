from datetime import date
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber


class ContactModel(BaseModel):
    first_name: str = Field(min_length=2, max_length=100)
    last_name: str = Field(min_length=2, max_length=100)
    email: EmailStr | None
    phone: PhoneNumber
    date_of_birth: date


class ContactUpdate(ContactModel):
    pass


class ContactResponse(ContactModel):
    id: int

    model_config = ConfigDict(from_attributes=True)
