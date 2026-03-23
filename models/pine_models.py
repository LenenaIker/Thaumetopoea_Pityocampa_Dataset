from dataclasses import dataclass
from models.nest_models import NestPlacementProfile


@dataclass
class PineDefinition:
    asset_path: str
    pine_type: str
    placement_profile: NestPlacementProfile
    max_nests: int

    source_mpu: float | None = None
    unit_correction_scale: float = 1.0
    canonical_world_height: float | None = None


@dataclass
class PineInstance:
    prim: object
    definition: PineDefinition
    position: tuple[float, float, float]
    scale: tuple[float, float, float]
    world_height_hint: float