from app.core.database import async_db
from app.repository.crud.user import UserCRUDRepository
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class UserSessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        session_id: str = request.cookies.get("session_id")

        async with async_db.session_factory() as db_session:
            user_repo = UserCRUDRepository(db_session)
            user = await user_repo.check_session(session_id=session_id)
            if user is None or session_id is None:
                user = await user_repo.add_user_session()
            request.state.user = user

        response = await call_next(request)
        response.set_cookie(
            key="session_id",
            value=str(user.session_id),
            httponly=True,
            max_age=86_400,  # время жизни 1 день
        )
        return response
