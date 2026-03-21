from config.settings import Settings

from core.generator import DatasetGenerator
from factories.camera_factory import CameraFactory
from factories.writer_factory import WriterFactory

from services.target_spawner import TargetSpawner
from services.ring_target_placer import RingTargetPlacer

from core.orchestrator import run_orchestrator
from core.stage import load_stage


from asset_constants import FOREST_01, TEMP_NESTS


def build_forest_base_generator(settings: Settings, app):
    camera_strategy = CameraFactory().create(settings.generation.camera_mode)
    writer_strategy = WriterFactory().create(settings.generation.writer_type)

    target_spawner = TargetSpawner(
        nest_assets = TEMP_NESTS,
        semantic_class = settings.dataset.target_class
    )

    target_placer = RingTargetPlacer(
        center=(0, 0, 3),
        radius=2.5,
        scale=(0.5, 0.5, 0.5),
    )

    return DatasetGenerator(
        app = app,
        settings = settings,
        scene_path = FOREST_01,
        camera_strategy = camera_strategy,
        writer_strategy = writer_strategy,
        orchestrator_runner = run_orchestrator,
        stage_loader = load_stage,
        target_spawner = target_spawner,
        target_placer = target_placer
    )