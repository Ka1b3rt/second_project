from app.core.database import sync_db
from app.models.parcel import Parcel, ParcelType
from app.models.user import User
from app.repository.crud.base import BaseCRUDRepository
from app.schemas.schemas import AddParcel, AddParcelResp, GetParcel, GetParcelTypes
from sqlalchemy import select, update


class ParcelCRUDRepository(BaseCRUDRepository):
    async def create_parcel(self, parcel: AddParcel, user: User) -> AddParcelResp:
        parcel_obj_dict = parcel.model_dump()
        parcel_obj_dict["user_id"] = user.session_id
        new_parcel = Parcel(**parcel_obj_dict)
        self.async_session.add(new_parcel)
        await self.async_session.commit()
        return AddParcelResp.model_validate(new_parcel)

    async def get_all_parcels(self) -> list[GetParcel]:
        return await self.get_all_items(Parcel, GetParcel)

    async def get_parcel_types(self) -> list[GetParcelTypes]:
        return await self.get_all_items(ParcelType, GetParcelTypes)

    async def get_parcels_by_user(self, user: User) -> list[GetParcel]:
        query = select(Parcel).where(Parcel.user_id == user.session_id)
        result = await self.async_session.execute(query)
        result_obj_list = result.scalars().all()
        return self._sqlalchemy_obj_list_to_pydantic(result_obj_list, GetParcel)

    @staticmethod
    def set_delivery_price(rate: float) -> None:
        with sync_db.session_factory() as session:
            query = update(Parcel).values(
                delivery_price=(Parcel.weight * 0.5 + Parcel.cost * 0.01) * rate
            )
            session.execute(query)
            session.commit()
