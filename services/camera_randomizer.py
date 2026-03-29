import omni.replicator.core as rep # pyright: ignore[reportMissingImports]

import random
import math

from config.settings import CameraRandomizationSettings

class CameraRandomizer:
    def __init__(self, settings: CameraRandomizationSettings):
        self.settings = settings

    def apply(self, camera):
        position_min = self.settings.position_min
        position_max = self.settings.position_max

        safe_position_min = (
            position_min[0],
            position_min[1],
            max(position_min[2], self.settings.min_height),
        )
        safe_position_max = (
            position_max[0],
            position_max[1],
            max(position_max[2], self.settings.min_height),
        )

        with camera:
            rep.modify.pose(
                position=rep.distribution.uniform(
                    safe_position_min,
                    safe_position_max,
                ),
                look_at=rep.distribution.uniform(
                    self.settings.look_at_min,
                    self.settings.look_at_max,
                ),
            )


    def apply_target_biased(
        self,
        camera,
        target_position,
        min_distance = 5.0,
        max_distance = 12.0,
        min_height_offset = 1.0,
        max_height_offset = 6.0,
        look_at_jitter_xy = 1.0,
        look_at_jitter_z = 0.8,
    ):
        tx, ty, tz = target_position

        yaw = random.uniform(0.0, 2.0 * math.pi)
        distance = random.uniform(min_distance, max_distance)
        height_offset = random.uniform(min_height_offset, max_height_offset)

        cx = tx + distance * math.cos(yaw)
        cy = ty + distance * math.sin(yaw)
        cz = max(tz + height_offset, self.settings.min_height)

        look_at = (
            tx + random.uniform(-look_at_jitter_xy, look_at_jitter_xy),
            ty + random.uniform(-look_at_jitter_xy, look_at_jitter_xy),
            tz + random.uniform(-look_at_jitter_z, look_at_jitter_z),
        )

        with camera:
            rep.modify.pose(
                position=(cx, cy, cz),
                look_at=look_at,
            )