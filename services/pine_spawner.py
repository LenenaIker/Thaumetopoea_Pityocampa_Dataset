import random
import omni.replicator.core as rep

from models.pine_models import PineDefinition, PineInstance


class PineSpawner:
    def __init__(self, pine_definitions: list[PineDefinition]):
        self.definitions = pine_definitions

    def spawn(self, count: int):
        instances = []

        for _ in range(count):
            definition = random.choice(self.definitions)

            prim = rep.create.from_usd(
                usd = definition.asset_path,
                semantics=[("class", "pine")],
                scale = (1, 1, 1),
                count=1,
            )

            instances.append(
                PineInstance(
                    prim = prim,
                    definition = definition,
                    position = (0, 0, 0), # se setea luego
                    scale = (1, 1, 1),
                    world_height_hint = definition.canonical_world_height or 0.0,
                )
            )

        return instances