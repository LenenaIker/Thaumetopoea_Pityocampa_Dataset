from dataclasses import dataclass
from models.nest_models import NestPlacementProfile


@dataclass(frozen=True)
class PineDefinition:
    asset_path: str
    pine_type: str
    placement_profile: NestPlacementProfile
    max_nests: int
    height_hint: float


@dataclass
class PineInstance:
    prim: object
    definition: object
    position: tuple[float, float, float]
    scale: tuple[float, float, float]
    height_hint: float