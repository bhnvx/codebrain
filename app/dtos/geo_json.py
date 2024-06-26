import dataclasses
from typing import Sequence, Annotated
from fastapi import Query

from app.entities.public.buildings import Buildings


@dataclasses.dataclass(kw_only=True)
class GeoJson:
    geometry: Sequence[Sequence[Sequence[float]]]
    properties: Buildings
    type: Annotated[str, Query(...)] = "Feature"
