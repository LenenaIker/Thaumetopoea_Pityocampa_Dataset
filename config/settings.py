from dataclasses import dataclass
from pathlib import Path


@dataclass
class RenderSettings:
    width: int
    height: int
    num_frames: int
    headless: bool
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
    output_dir: Path
    warmup_steps: int = 100
    target_class: str = "nest"


@dataclass
class GenerationSettings:
    distractor_type: str = "forest"
    writer_type: str = "basic" # basic | coco | kitti
    camera_mode: str = "fixed" # fixed | random | drone



@dataclass
class Settings:
    render: RenderSettings
    dataset: DatasetSettings
    generation: GenerationSettings

    def to_launch_config(self) -> dict:
        return self.render.to_launch_config()


def build_settings(args) -> Settings:
    return Settings(
        render=RenderSettings(
            width=args.width,
            height=args.height,
            num_frames=args.num_frames,
            headless=args.headless,
            renderer=getattr(args, "renderer", "RayTracedLighting"),
            rt_subframes=getattr(args, "rt_subframes", 1),
        ),
        dataset=DatasetSettings(
            output_dir=Path(args.data_dir).expanduser().resolve(),
            warmup_steps=getattr(args, "warmup_steps", 100),
            target_class=getattr(args, "target_class", "nest"),
        ),
        generation=GenerationSettings(
            distractor_type=getattr(args, "distractor_type", "forest"),
            writer_type=getattr(args, "writer_type", "basic"),
            camera_mode=getattr(args, "camera_mode", "fixed"),
        ),
    )