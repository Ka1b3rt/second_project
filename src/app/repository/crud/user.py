from uuid import UUID

from app.models.user import User
from sqlalchemy import select

from .base import BaseCRUDRepository


class UserCRUDRepository(BaseCRUDRepository):
    async def add_user_session(self) -> User:
        """Add new user with auto-generated UUID in DB"""
        new_user = User()
        self.async_session.add(new_user)
        await self.async_session.commit()
        return new_user

    async def check_session(self, session_id: str) -> User | None:
        """Checks whether user exist"""
        if session_id is None:
            return None
        query = select(User).where(User.session_id == UUID(session_id))
        result = await self.async_session.execute(query)
        return result.scalar_one_or_none()
