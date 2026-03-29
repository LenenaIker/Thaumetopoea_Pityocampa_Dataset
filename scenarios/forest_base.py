from config.settings import Settings

from core.generator import DatasetGenerator
from factories.camera_factory import CameraFactory
from factories.writer_factory import WriterFactory

from core.orchestrator import run_orchestrator
from core.stage import load_stage

from asset_constants import FOREST_01, TEMP_NESTS, NESTS
from asset_constants import PINES, SMALL_PINES

from models.pine_models import PineDefinition
from models.nest_models import NestPlacementProfile

from services.pine_spawner import PineSpawner
from services.pine_placer import PinePlacer
from services.nest_spawner import NestSpawner


TIP_PROFILE = NestPlacementProfile(
    min_height_ratio = 0.85,
    max_height_ratio = 0.98,
    min_radial_offset = 0.0,
    max_radial_offset = 0.2,
)

BRANCH_PROFILE = NestPlacementProfile(
    min_height_ratio = 0.6,
    max_height_ratio = 0.9,
    min_radial_offset = 0.3,
    max_radial_offset = 1.0,
)

pine_definitions = [
    PineDefinition(
        asset_path = p,
        pine_type = "arrow",
        placement_profile = TIP_PROFILE,
        max_nests = 1,
    )
    for p in SMALL_PINES
] + [
    PineDefinition(
        asset_path = p,
        pine_type = "branchy",
        placement_profile = BRANCH_PROFILE,
        max_nests = 5,
    )
    for p in PINES
]


def build_forest_base_generator(settings: Settings, app):
    camera_strategy = CameraFactory().create("fixed")
    writer_strategy = WriterFactory().create(settings.generation.writer_type)

    pine_spawner = PineSpawner(pine_definitions = pine_definitions)
    pine_placer = PinePlacer(
        area_radius = 50,
        min_distance = 3,
        min_scale = 0.5,
        max_scale = 1.5,
        max_attempts = 20
    )

    nest_spawner = NestSpawner(
        nest_assets = NESTS,
        semantic_class = settings.dataset.target_class
    )

    return DatasetGenerator(
        app = app,
        settings = settings,
        scene_path = FOREST_01,
        camera_strategy = camera_strategy,
        writer_strategy = writer_strategy,
        orchestrator_runner = run_orchestrator,
        stage_loader = load_stage,
        pine_spawner = pine_spawner,
        pine_placer = pine_placer,
        nest_spawner = nest_spawner
    )
