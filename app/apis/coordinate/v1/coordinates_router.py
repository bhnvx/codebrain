from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.dtos.coordinates_request import CoordinatesRequest
from app.dtos.coordinates_response import GeoJsonResponse
from app.services.coordinates_service import get_geojson_data_by_coordinates

from app.utils.db_ import get_db_session

router = APIRouter(
    prefix="/api/v1/coordinates", tags=["Coordinates APIS"], redirect_slashes=False
)


@router.get(
    "/",
    description="위경도 값을 받아 이에 따른 부동산 목록을 조회합니다.",
    response_class=ORJSONResponse,
)
async def api_get_coordinates(
    coordinates: Annotated[CoordinatesRequest, Depends()],
    db: AsyncSession = Depends(get_db_session),
) -> GeoJsonResponse:
    result = await get_geojson_data_by_coordinates(db=db, coordinates=coordinates)
    if result:
        return GeoJsonResponse(features=result)
    return GeoJsonResponse(features=())
