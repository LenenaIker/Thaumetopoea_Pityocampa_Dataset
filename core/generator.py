from config.settings import Settings

from strategies.camera_strategy import CameraStrategy
from strategies.writer_strategy import WriterStrategy

from services.nest_placer import NestOnPinePlacer
from core.usd_metrics import UsdMetricResolver

import random
import omni.replicator.core as rep
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
        # self.nest_placer = nest_placer

    def run(self):
        output_dir = Path(self.settings.dataset.output_dir)
        output_dir.mkdir(parents = True, exist_ok = True)
        print(f"Output dir: {output_dir}")

        stage = self.stage_loader(self.scene_path)
        resolver = UsdMetricResolver(stage)

        for definition in self.pine_spawner.definitions:
            asset_mpu, unit_correction_scale, canonical_world_height = resolver.resolve(definition.asset_path)
            definition.source_mpu = asset_mpu
            definition.unit_correction_scale = unit_correction_scale
            definition.canonical_world_height = canonical_world_height


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

            
            num_pines = 5 #random.randint(5, 10)
            pines = self.pine_spawner.spawn(num_pines)
            self.pine_placer.place(pines)

            # self.app.update()
            # self._update_pine_heights(pines)

            for pine in pines:
                profile = pine.definition.placement_profile
                num_nests = random.randint(1, profile.max_nests)

                placer = NestOnPinePlacer(placement_profile = profile)

                for _ in range(num_nests):
                    nest = self.nest_spawner.spawn_one()
                    placer.place_one(nest, pine)


            with rep.trigger.on_frame(num_frames = self.settings.render.num_frames):
                pass


        self.orchestrator_runner(self.app)
        self.app.update()
        print("DatasetGenerator: Done.")