import random
import math
import omni.replicator.core as rep

from models.pine_models import PineInstance
from models.nest_models import NestPlacementProfile


class NestOnPinePlacer:
    def __init__(
        self,
        placement_profile: NestPlacementProfile,
        min_scale = 0.15,
        max_scale = 0.35,
    ):
        self.place_prof = placement_profile
        self.min_scale = min_scale
        self.max_scale = max_scale

    def place_one(self, nest, pine_instance: PineInstance):
        position, scale = self.sample_pose(pine_instance)
        self.apply_pose(nest, position, scale)

    def sample_pose(self, pine_instance: PineInstance):
        px, py, pz = pine_instance.position
        tree_height = pine_instance.world_height_hint

        if tree_height is None or tree_height <= 0.0:
            raise ValueError(
                f"Invalid pine world_height_hint for nest placement: {tree_height}"
            )

        height = random.uniform(
            self.place_prof.min_height_ratio * tree_height,
            self.place_prof.max_height_ratio * tree_height,
        )

        angle = random.uniform(0.0, 2.0 * math.pi)
        radial = random.uniform(
            self.place_prof.min_radial_offset,
            self.place_prof.max_radial_offset
        )

        x = px + radial * math.cos(angle)
        y = py + radial * math.sin(angle)
        z = pz + height

        s = random.uniform(self.min_scale, self.max_scale)

        return (x, y, z), (s, s, s)

    def apply_pose(self, nest, position, scale):
        with nest:
            rep.modify.pose(
                position = position,
                scale = scale,
            )