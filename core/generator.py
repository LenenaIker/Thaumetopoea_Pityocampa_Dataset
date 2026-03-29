from config.settings import Settings

from strategies.camera_strategy import CameraStrategy
from strategies.writer_strategy import WriterStrategy

from services.nest_placer import NestOnPinePlacer
from services.camera_randomizer import CameraRandomizer
from core.usd_metrics import UsdMetricResolver

import random
import omni.replicator.core as rep # pyright: ignore[reportMissingImports]
from pathlib import Path



class DatasetGenerator:
    def __init__(
        self,
        app,
        settings: Settings,
        scene_path: str | Path,
        camera_strategy: CameraStrategy,
        writer_strategy: WriterStrategy,
        orchestrator_runner,
        stage_loader,
        pine_spawner,
        pine_placer,
        nest_spawner
        # nest_placer
    ):
        self.app = app
        self.settings = settings
        self.scene_path = scene_path

        self.camera_strategy = camera_strategy
        self.writer_strategy = writer_strategy
        
        self.orchestrator_runner = orchestrator_runner
        self.stage_loader = stage_loader

        self.pine_spawner = pine_spawner
        self.pine_placer = pine_placer
        self.nest_spawner = nest_spawner

    def run(self):
        output_dir = Path(self.settings.dataset.output_dir)
        output_dir.mkdir(parents = True, exist_ok = True)
        print(f"Output dir: {output_dir}")

        stage = self.stage_loader(self.scene_path)
        self._resolve_pine_metrics(stage)

        for _ in range(self.settings.dataset.warmup_steps):
            self.app.update()


        with rep.new_layer(name = "Replicator_layer"):

            camera = self.camera_strategy.create_camera()

            render_product = rep.create.render_product(
                name = "CameraRenderProduct",
                camera = camera,
                resolution = (self.settings.render.width, self.settings.render.height)
            )

            writer = self.writer_strategy.initialize(
                str(self.settings.dataset.output_dir)
            )
            writer.attach([render_product])


            # TODO: Es más barato rep.create.sphere()?
            # TODO: Si uso rep.create.from_dir(), ¿puedo declarar todos los distractors a la vez?
            # TODO: ¿rep.distribution.choice() puede servirme para seleccionar los pinos donde generar nidos aleatoriamente?


            placed_pines = self._spawn_and_place_pines()
            self._spawn_and_place_nests(placed_pines)

            with rep.trigger.on_frame(num_frames = self.settings.render.num_frames):
                self._register_camera_behavior(camera)

        self.orchestrator_runner(self.app)
        self.app.update()
        print("DatasetGenerator: Done.")

    def _resolve_pine_metrics(self, stage):
        resolver = UsdMetricResolver(stage)

        for definition in self.pine_spawner.definitions:
            asset_mpu, unit_correction_scale, canonical_world_height = resolver.resolve(
                definition.asset_path
            )
            definition.source_mpu = asset_mpu
            definition.unit_correction_scale = unit_correction_scale
            definition.canonical_world_height = canonical_world_height

    def _spawn_and_place_pines(self):
        num_pines = random.randint(20, 50)
        spawned_pines = self.pine_spawner.spawn(num_pines)
        placed_pines = self.pine_placer.place(spawned_pines)

        print(
            f"[GENERATOR] Pines spawned={len(spawned_pines)} placed={len(placed_pines)} "
            f"failed={len(spawned_pines) - len(placed_pines)}"
        )

        return placed_pines

    def _spawn_and_place_nests(self, pines):
        for pine in pines:
            profile = pine.definition.placement_profile
            max_nests = pine.definition.max_nests

            if random.choice([True, False]): # Add nests to this tree? 50%
                num_nests = random.randint(1, max_nests)

                placer = NestOnPinePlacer(placement_profile=profile)

                for _ in range(num_nests):
                    nest = self.nest_spawner.spawn_one()
                    placer.place_one(nest, pine)
    
    def _register_camera_behavior(self, camera):
        camera_mode = self.settings.generation.camera_mode

        if camera_mode == "fixed":
            return

        if camera_mode == "random":
            randomizer = CameraRandomizer(settings = self.settings.generation.camera_randomization)
            randomizer.apply(camera)
            return

        raise ValueError(f"Unsupported camera_mode: {camera_mode}")