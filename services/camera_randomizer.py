import omni.replicator.core as rep

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