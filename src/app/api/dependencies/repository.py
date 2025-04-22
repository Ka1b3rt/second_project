import typing

import fastapi
from app.api.dependencies.session import get_async_session
from app.repository.crud.base import BaseCRUDRepository
from sqlalchemy.ext.asyncio import AsyncSession


def get_repository(
    repo_type: typing.Type[BaseCRUDRepository],
) -> typing.Callable[[AsyncSession], BaseCRUDRepository]:
    def _get_repo(
        async_session: AsyncSession = fastapi.Depends(get_async_session),
    ) -> BaseCRUDRepository:
        return repo_type(async_session=async_session)

    return _get_repo
