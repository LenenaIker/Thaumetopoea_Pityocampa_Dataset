import random
import omni.replicator.core as rep # pyright: ignore[reportMissingImports]

class NestSpawner:
    def __init__(self, nest_assets: list[str], semantic_class: str):
        self.nest_assets = nest_assets
        self.semantic_class = semantic_class

    def spawn_one(self):
        asset_path = random.choice(self.nest_assets)
        return rep.create.from_usd(
            asset_path,
            semantics=[("class", self.semantic_class)],
            count=1,
        )