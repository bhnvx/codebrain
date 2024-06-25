import dataclasses
from typing import Literal, Sequence

from .geo_metry import GeoMetry


@dataclasses.dataclass
class GeoMetryResponse:
    type = "FeatureCollection"
    features: GeoMetry
    # properties = None
