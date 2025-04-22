import logging

from app.api.dependencies.cache import get_redis_client
from app.api.dependencies.repository import get_repository
from app.api.dependencies.user import get_current_user
from app.core.logging_config import setup_logging
from app.models.user import User
from app.repository.crud.parcel import ParcelCRUDRepository
from app.schemas.schemas import AddParcel, AddParcelResp, GetParcel
from app.utils.cache import (
    cache_get_list_pydantic_models,
    cache_set_list_pydantic_models,
)
from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.exc import IntegrityError

from redis.asyncio import Redis

setup_logging(level=logging.INFO)
router = APIRouter()


@router.post("/parcel", response_model=AddParcelResp, summary="Добавление посылки")
async def add_parcel(
    parcel: AddParcel,
    parcel_repo: ParcelCRUDRepository = Depends(get_repository(ParcelCRUDRepository)),
    user: User = Depends(get_current_user),
    redis: Redis = Depends(get_redis_client),
):
    try:
        new_parcel: AddParcelResp = await parcel_repo.create_parcel(parcel, user)
        await redis.delete(str(user.session_id))
        return new_parcel
    except IntegrityError as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=type(e).__name__) from e


@router.get("/parcel", summary="Получение всех посылок")
async def get_all_parcels(
    parcel_repo: ParcelCRUDRepository = Depends(get_repository(ParcelCRUDRepository)),
    user: User = Depends(get_current_user),
    redis: Redis = Depends(get_redis_client),
):
    parcels = await cache_get_list_pydantic_models(
        str(user.session_id), GetParcel, redis
    )
    if parcels:
        return parcels
    logging.info(
        f"Cache entry not found for {user.session_id=}, loading from from DB..."
    )
    parcels = await parcel_repo.get_parcels_by_user(user)
    await cache_set_list_pydantic_models(user.session_id, parcels, redis)

    return parcels


@router.get("/parcel_types", summary="Получение всех типов посылок")
async def get_parcel_types(
    parcel_repo: ParcelCRUDRepository = Depends(get_repository(ParcelCRUDRepository)),
):
    return await parcel_repo.get_parcel_types()
