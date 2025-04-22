# src/app/services/session.py
from typing import Optional

from app.core.database import async_db
from app.models.user import User
from app.repository.crud.user import UserCRUDRepository

class SessionService:
    def __init__(self):
        self.session_timeout = 86_400  # 1 день
    
    async def get_or_create_session(self, session_id: Optional[str] = None) -> User:
        """Получает существующую сессию или создает новую"""
        async with async_db.session_factory() as db_session:
            user_repo = UserCRUDRepository(db_session)
            
            if session_id:
                user = await user_repo.check_session(session_id=session_id)
                if user:
                    return user
            
            # Создаем новую сессию, если не найдена существующая
            return await user_repo.add_user_session()
    
    async def validate_session(self, session_id: str) -> bool:
        """Проверяет валидность сессии"""
        async with async_db.session_factory() as db_session:
            user_repo = UserCRUDRepository(db_session)
            user = await user_repo.check_session(session_id=session_id)
            return user is not None