import random
import math
import omni.replicator.core as rep


class PinePlacer:
    def __init__(
        self,
        area_radius=10.0,
        min_distance=4.0,
        min_scale=0.8,
        max_scale=1.3
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

                    variation_scale = random.uniform(self.min_scale, self.max_scale)
                    final_scale = pine.definition.unit_correction_scale * variation_scale

                    with pine.prim:
                        rep.modify.pose(
                            position=(x, y, 0),
                            scale=(final_scale, final_scale, final_scale),
                        )

                    pine.position = (x, y, 0)
                    pine.scale = (final_scale, final_scale, final_scale)

                    base_height = pine.definition.canonical_world_height or 0.0
                    pine.world_height_hint = base_height * variation_scale

                    print(
                        f"[PINE PLACE] asset={pine.definition.asset_path} "
                        f"pos={(x, y, 0)} scale={final_scale:.6f} "
                        f"world_height={pine.world_height_hint:.3f}"
                    )
                    break

    def _is_far_enough(self, pos, existing):
        for ex in existing:
            if math.dist(pos, ex) < self.min_distance:
                return False
        return True