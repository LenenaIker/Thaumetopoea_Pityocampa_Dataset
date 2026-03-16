from dataclasses import dataclass
from pathlib import Path


@dataclass
class DatasetConfig:
    headless: bool = False
    width: int = 960
    height: int = 544
    num_frames: int = 1000
    output_dir: Path = Path("./output")
    distractor_type: str = "forest"
    writer_type: str = "coco" # "kitti"
    target_class: str = "nest"