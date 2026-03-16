from dataclasses import dataclass

@dataclass
class AssetCatalog:
    environment_path: str
    nest_assets: list[str]
    nest_distractor_assets: list[str]
    pine_assets: list[str]
    distractor_assets: list[str]
    textures: list[str]