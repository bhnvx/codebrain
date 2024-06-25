import dataclasses
from typing import Annotated

from fastapi import Query


@dataclasses.dataclass
class CoordinatesRequest:
    longitude: Annotated[
        float, Query(..., example=127.00592, gt=124, lt=132, description="경도")
    ]
    latitude: Annotated[
        float, Query(..., example=37.49006, gt=33, lt=39, description="위도")
    ]
