from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import EmailStr

from src.repository.contacts import ContactRepository
from src.schemas.contacts import ContactModel

from src.utils.birthday_check import is_birthday_in_next_N_days


class ContactService:
    def __init__(self, db: AsyncSession) -> None:
        self.repository = ContactRepository(db)

    async def get_contacts(
        self,
        skip: int,
        limit: int,
        first_name: str | None,
        last_name: str | None,
        email: EmailStr | None,
    ):
        contacts = await self.repository.get_contacts(skip, limit)

        if first_name:
            contacts = [
                contact for contact in contacts if contact.first_name == first_name
            ]

        if last_name:
            contacts = [
                contact for contact in contacts if contact.last_name == last_name
            ]

        if email:
            contacts = [contact for contact in contacts if contact.email == email]

        return contacts

    async def get_contacts_birthday_next_7_days(self, skip: int, limit: int):
        contacts = await self.repository.get_contacts(skip, limit)
        contacts = [
            contact
            for contact in contacts
            if is_birthday_in_next_N_days(7, contact.date_of_birth)
        ]

        return contacts

    async def get_contact(self, contact_id: int):
        return await self.repository.get_contact_by_id(contact_id)

    async def create_contact(self, body: ContactModel):
        return await self.repository.create_contact(body)

    async def update_contact(self, contact_id: int, body: ContactModel):
        return await self.repository.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.repository.remove_contact(contact_id)
