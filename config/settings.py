from dataclasses import dataclass, field, fields
from pathlib import Path

@dataclass
class RenderSettings:
    width: int = 960
    height: int = 544
    num_frames: int = 1000
    headless: bool = False
    renderer: str = "RayTracedLighting"
    rt_subframes: int = 1

    def to_launch_config(self) -> dict:
        return {
            "width": self.width,
            "height": self.height,
            "headless": self.headless,
            "renderer": self.renderer,
        }

@dataclass
class DatasetSettings:
    output_dir: Path = field(default_factory = lambda: Path.cwd() / "_tp_output")
    warmup_steps: int = 100
    target_class: str = "nest"

@dataclass
class GenerationSettings:
    distractor_type: str = "forest"
    writer_type: str = "basic"
    camera_mode: str = "fixed"


@dataclass
class Settings:
    render: RenderSettings = field(default_factory = RenderSettings)
    dataset: DatasetSettings = field(default_factory = DatasetSettings)
    generation: GenerationSettings = field(default_factory = GenerationSettings)

    def to_launch_config(self) -> dict:
        return self.render.to_launch_config()



def pick(dataclass_type, values: dict) -> dict:
    valid_names = {f.name for f in fields(dataclass_type)}
    return {
        k: v
        for k, v in values.items()
        if k in valid_names and v is not None
    }

def build_settings(args) -> Settings:
    raw = vars(args).copy()

    if raw.get("data_dir") is not None:
        raw["output_dir"] = Path(raw.pop("data_dir")).expanduser().resolve()

    return Settings(
        render = RenderSettings(**pick(RenderSettings, raw)),
        dataset = DatasetSettings(**pick(DatasetSettings, raw)),
        generation = GenerationSettings(**pick(GenerationSettings, raw)),
    )