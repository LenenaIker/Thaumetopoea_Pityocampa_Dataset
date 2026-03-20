
from core.generator import DatasetGenerator
from factories.camera_factory import CameraFactory
from factories.writer_factory import WriterFactory

from core.orchestrator import run_orchestrator
from core.stage import load_stage

from asset_constants import FOREST_01


def build_forest_base_generator(settings, app):
    camera_strategy = CameraFactory().create(settings.generation.camera_mode)
    writer_strategy = WriterFactory().create(settings.generation.writer_type)

    return DatasetGenerator(
        app,
        settings = settings,
        scene_path = FOREST_01,
        camera_strategy = camera_strategy,
        writer_strategy = writer_strategy,
        orchestrator_runner = run_orchestrator,
        stage_loader = load_stage
    )