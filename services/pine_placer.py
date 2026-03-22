import random
import math
import omni.replicator.core as rep


class PinePlacer:
    def __init__(
        self,
        area_radius=15.0,
        min_distance=2.5,
        min_scale=0.01,
        max_scale=0.015,
    ):
        self.area_radius = area_radius
        self.min_distance = min_distance
        self.min_scale = min_scale
        self.max_scale = max_scale

    def place(self, pine_instances):
        placed_positions = []

        for pine in pine_instances:
            for _ in range(10): # retry attempts
                angle = random.uniform(0, 2 * math.pi)
                r = random.uniform(0, self.area_radius)

                x = r * math.cos(angle)
                y = r * math.sin(angle)

                if self._is_far_enough((x, y), placed_positions):
                    placed_positions.append((x, y))

                    scale = random.uniform(self.min_scale, self.max_scale)

                    with pine.prim:
                        rep.modify.pose(
                            position=(x, y, 0),
                            scale=(scale, scale, scale),
                        )

                    pine.position = (x, y, 0)
                    pine.scale = (scale, scale, scale)
                    
                    
                    pine.height_hint = pine.definition.height_hint * scale

                    print(
                        f"[PINE] asset={pine.definition.asset_path} "
                        f"pos={(x, y, 0)} scale={scale:.4f} "
                        f"height_hint_eff={pine.height_hint:.4f}"
                    )

                    break

    def _is_far_enough(self, pos, existing):
        for ex in existing:
            if math.dist(pos, ex) < self.min_distance:
                return False
        return True