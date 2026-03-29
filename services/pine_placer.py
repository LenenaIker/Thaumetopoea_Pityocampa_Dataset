import random
import math
import omni.replicator.core as rep


class PinePlacer:
    def __init__(
        self,
        area_radius=10.0,
        min_distance=4.0,
        min_scale=0.8,
        max_scale=1.3,
        max_attempts=10,
    ):
        self.area_radius = area_radius
        self.min_distance = min_distance
        self.min_scale = min_scale
        self.max_scale = max_scale
        self.max_attempts = max_attempts

    def place(self, pine_instances):
        placed_pines = []
        placed_positions = []

        for pine in pine_instances:
            sampled_position = self._sample_world_position(placed_positions)

            if sampled_position is None:
                print(
                    f"[PINE PLACE][WARN] Could not place asset={pine.definition.asset_path} "
                    f"after {self.max_attempts} attempts"
                )

                with pine.prim: # FIXME: Solución simple pero incorrecta. En lugar de crear muchos pinos y luego ocultar los que no pueda colocar, debería de decirdir posiciones primero y luego spawnear dependiendo de las posiciones disponibles.
                    rep.modify.visibility(False)
                
                continue

            x, y, z = sampled_position
            variation_scale = random.uniform(self.min_scale, self.max_scale)
            final_scale = pine.definition.unit_correction_scale * variation_scale

            with pine.prim:
                rep.modify.pose(
                    position=(x, y, z),
                    scale=(final_scale, final_scale, final_scale),
                )

            pine.position = (x, y, z)
            pine.scale = (final_scale, final_scale, final_scale)

            base_height = pine.definition.canonical_world_height or 0.0
            pine.world_height_hint = base_height * variation_scale

            placed_positions.append((x, y))
            placed_pines.append(pine)


        return placed_pines

    def _sample_world_position(self, existing_positions):
        for _ in range(self.max_attempts):
            angle = random.uniform(0.0, 2.0 * math.pi)
            r = random.uniform(0.0, self.area_radius)

            x = r * math.cos(angle)
            y = r * math.sin(angle)

            if self._is_far_enough((x, y), existing_positions):
                return (x, y, 0.0)

        return None

    def _is_far_enough(self, pos, existing):
        for ex in existing:
            if math.dist(pos, ex) < self.min_distance:
                return False
        return True