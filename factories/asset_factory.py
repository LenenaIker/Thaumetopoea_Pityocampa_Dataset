from models.asset_models import AssetCatalog
import omni.replicator.core as rep

class AssetFactory:
    def __init__(self, catalog: AssetCatalog):
        self.catalog = catalog

    def create_targets(self, semantic_class: str):
        objs = [
            rep.create.from_usd(path, semantics=[("class", semantic_class)], count=1)
            for path in self.catalog.nest_assets
        ]
        
        return rep.create.group(objs)

    def create_distractors(self):
        objs = [rep.create.from_usd(path, count=1) for path in self.catalog.distractor_assets]
        return rep.create.group(objs)