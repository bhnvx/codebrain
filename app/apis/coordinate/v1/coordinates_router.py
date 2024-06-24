from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse

from app.dtos.coordinates_request import CoordinatesRequest


router = APIRouter(prefix="/api/v1/coordinates", tags=["Coordinates APIS"], redirect_slashes=False)


@router.get(
    "/radius",
    description="radius에 따른 부동산 목록을 조회합니다.",
    response_class=ORJSONResponse,
)
async def api_get_categories_radius(coordinates: Annotated[CoordinatesRequest, Depends()]) -> None:
    return 
