from dataclasses import dataclass

@dataclass(frozen=True)
class NestPlacementProfile:
    min_height_ratio: float
    max_height_ratio: float
    min_radial_offset: float
    max_radial_offset: float

@dataclass
class NestInstance:
    prim: object
    position: tuple[float, float, float]
    scale: tuple[float, float, float]
    pine_position: tuple[float, float, float]
