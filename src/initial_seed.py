from app.core.database import sync_db
from app.models.parcel import ParcelType, TypeType
from sqlalchemy import delete, select, text


def check_is_seeded() -> bool:
    with sync_db.session_factory() as session:
        query = select(ParcelType)
        result = session.execute(query)
        result_obj = result.scalars().all()

        try:
            assert len(result_obj) == len(TypeType)
            for obj in result_obj:
                assert obj.id in range(1, len(TypeType) + 1, 1)
                assert obj.type in [_ for _ in TypeType]
            return True
        except AssertionError:
            return False


def seed_parcel_types():
    if check_is_seeded():
        print("DB seeded properly!")
    else:
        print("Start initial_seed...")
        with sync_db.session_factory() as session:
            query = delete(ParcelType)
            session.execute(query)
            session.execute(text("ALTER SEQUENCE parcel_type_id_seq RESTART WITH 1"))
            for type in TypeType:
                session.add(ParcelType(type=type))
            session.commit()
        print("Seeding done!")


seed_parcel_types()
