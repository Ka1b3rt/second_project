import typing

import pydantic
from app.models.base import SQLAlchemyBaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

TModel = typing.TypeVar("TModel", bound=pydantic.BaseModel)


class BaseCRUDRepository:
    def __init__(self, async_session: AsyncSession):
        self.async_session = async_session

    @staticmethod
    def _sqlalchemy_obj_list_to_pydantic(
        obj_list: typing.Sequence[SQLAlchemyBaseModel],
        obj_type_target: typing.Type[TModel],
    ) -> list[TModel]:
        return [obj_type_target.model_validate(obj) for obj in obj_list]

    async def get_all_items(
        self,
        sqlalchemy_model: typing.Type[SQLAlchemyBaseModel],
        pydantic_schema: typing.Type[pydantic.BaseModel],
    ) -> list[TModel]:
        query = select(sqlalchemy_model)
        result = await self.async_session.execute(query)
        result_obj_list = result.scalars().all()
        return self._sqlalchemy_obj_list_to_pydantic(result_obj_list, pydantic_schema)
