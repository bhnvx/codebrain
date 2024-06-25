from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.dtos.coordinates_request import CoordinatesRequest
from app.dtos.geometry_response import GeoMetryResponse
from app.entities.public.controller import CONTROLLER_TL_SPBD_BULD_28000

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
) -> None:
    await CONTROLLER_TL_SPBD_BULD_28000(db).get_multipolygon_by_coordinates_requests(
        coordinates
    )
    return
