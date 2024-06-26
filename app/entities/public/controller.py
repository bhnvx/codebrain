import json
from typing import List

from sqlalchemy import select
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.public.tables import TABLE_TL_SPBD_BULD_28000
from app.dtos.coordinates_request import CoordinatesRequest


class CONTROLLER_TL_SPBD_BULD_28000:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def find_area_within_radius_by_coordinates(
        self, coordinates: CoordinatesRequest, radius=500
    ) -> List:
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
        return tuple(
            {
                "properties": {
                    "id": i[0],
                    "buld_nm": i[1],
                    "buld_nm_dc": i[2],
                    "pos_bul_nm": i[3],
                    "gro_flo_co": i[4],
                },
                "geometry": {
                    "type": json.loads(i[5])["type"],
                    "coordinates": json.loads(i[5])["coordinates"],
                },
            }
            for i in datas
        )
