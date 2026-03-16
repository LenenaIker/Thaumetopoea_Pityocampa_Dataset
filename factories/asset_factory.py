from config.asset_catalog import AssetCatalog

class AssetFactory:
    def __init__(self, catalog: AssetCatalog):
        self.catalog = catalog

    def create_targets(self, rep, semantic_class: str):
        objs = [
            rep.create.from_usd(path, semantics=[("class", semantic_class)], count=1)
            for path in self.catalog.target_assets
        ]
        return rep.create.group(objs)

    def create_distractors(self, rep):
        objs = [rep.create.from_usd(path, count=1) for path in self.catalog.distractor_assets]
        return rep.create.group(objs)