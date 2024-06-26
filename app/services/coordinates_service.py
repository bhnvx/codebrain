from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.public.controller import CONTROLLER_TL_SPBD_BULD_28000
from app.dtos.coordinates_request import CoordinatesRequest


async def get_geojson_data_by_coordinates(
    db: AsyncSession, coordinates: CoordinatesRequest
):
    return await CONTROLLER_TL_SPBD_BULD_28000(
        db
    ).find_area_within_radius_by_coordinates(coordinates)
