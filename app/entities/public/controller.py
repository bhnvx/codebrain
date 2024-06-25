from sqlalchemy import select
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.asyncio import AsyncSession

from shapely import wkt

from app.entities.public.tables import TABLE_TL_SPBD_BULD_28000
from app.dtos.coordinates_request import CoordinatesRequest


class CONTROLLER_TL_SPBD_BULD_28000:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_multipolygon_by_coordinates_requests(
        self, coordinates: CoordinatesRequest, radius=500
    ):
        query = select(
            TABLE_TL_SPBD_BULD_28000.id,
            TABLE_TL_SPBD_BULD_28000.buld_nm,
            TABLE_TL_SPBD_BULD_28000.buld_nm_dc,
            TABLE_TL_SPBD_BULD_28000.pos_bul_nm,
            TABLE_TL_SPBD_BULD_28000.gro_flo_co,
            func.ST_AsGeoJSON(
                func.ST_Transform(TABLE_TL_SPBD_BULD_28000.geom, 4329)
            ).label("coordinates"),
        ).filter(
            func.ST_DWithin(
                TABLE_TL_SPBD_BULD_28000.geom,
                func.ST_Transform(
                    func.ST_SetSRID(
                        func.ST_MakePoint(coordinates.longitude, coordinates.latitude),
                        4329,
                    ),
                    5179,
                ),
                radius,
            )
        )

        result = await self.db.execute(query)
        datas = result.fetchall()

        print(datas[0].coordinates)
