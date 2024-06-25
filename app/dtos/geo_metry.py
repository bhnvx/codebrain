import dataclasses
from typing import Literal, Sequence


@dataclasses.dataclass(kw_only=True)
class GeoMetry:
    type = "Feature"
    coordinates: Sequence[Sequence[Sequence[float]]]
