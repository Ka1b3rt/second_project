import json
from typing import Type, TypeVar

from app.schemas.schemas import BaseSchemaModel

from redis.asyncio import Redis

TModel = TypeVar("TModel", bound=BaseSchemaModel)


def serialize_list(data: list[TModel]) -> str:
    data_converted = [_.model_dump_json() for _ in data]
    parcels_str = json.dumps(data_converted)
    return parcels_str


def deserialize_list(data, model: Type[TModel]) -> list[TModel]:
    data_list_str = json.loads(data)
    data_list_dict = [json.loads(_) for _ in data_list_str]
    converted_data: list[TModel] = [model(**_) for _ in data_list_dict]
    return converted_data


async def cache_set_list_pydantic_models(key, data: list, redis: Redis) -> None:
    data_str = serialize_list(data)
    await redis.set(str(key), data_str)


async def cache_get_list_pydantic_models(
    key, model: Type[TModel], redis: Redis
) -> list[TModel] | None:
    data = await redis.get(str(key))
    if data:
        data_obj_list = deserialize_list(data, model)
        return data_obj_list
    else:
        return None
