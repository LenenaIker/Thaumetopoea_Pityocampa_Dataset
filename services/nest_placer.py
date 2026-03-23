import random
import math
import omni.replicator.core as rep

from models.pine_models import PineInstance
from models.nest_models import NestPlacementProfile


class NestOnPinePlacer:
    def __init__(
        self,
        placement_profile: NestPlacementProfile,
        # min_height_ratio=0.6,
        # max_height_ratio=0.9,
        # min_radial_offset=0.2,
        # max_radial_offset=0.8,
        min_scale = 0.15,
        max_scale = 0.35,
    ):
        self.place_prof = placement_profile
        self.min_scale = min_scale
        self.max_scale = max_scale

    def place_one(self, nest, pine_instance: PineInstance):
        px, py, pz = pine_instance.position
        tree_height = pine_instance.world_height_hint

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

        with nest:
            rep.modify.pose(
                position=(x, y, z),
                scale=(s, s, s),
            )