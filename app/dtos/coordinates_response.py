import dataclasses
from typing import Sequence, Annotated
from fastapi import Query

from app.dtos.geo_json import GeoJson


@dataclasses.dataclass
class GeoJsonResponse:
    features: Sequence[GeoJson]
    type: Annotated[str, Query(...)] = "FeatureCollection"
