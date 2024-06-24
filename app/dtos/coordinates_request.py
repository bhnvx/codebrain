import dataclasses
from typing import Annotated

from fastapi import Query


@dataclasses.dataclass
class CoordinatesRequest:
    longitude: Annotated[float, Query(..., example=127.00592, gt=124, lt=132)]
    latitude: Annotated[float, Query(..., example=37.49006, gt=33, lt=39)]
    radius: Annotated[int, Query(..., example=500, gt=1, lt=1000)]
