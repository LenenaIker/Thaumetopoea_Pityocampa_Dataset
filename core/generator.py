from config.settings import Settings

from strategies.camera_strategy import CameraStrategy
from strategies.writer_strategy import WriterStrategy

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
        target_spawner,
        target_placer
    ):
        self.app = app
        self.settings = settings
        self.scene_path = scene_path

        self.camera_strategy = camera_strategy
        self.writer_strategy = writer_strategy
        self.orchestrator_runner = orchestrator_runner
        self.stage_loader = stage_loader
        self.target_spawner = target_spawner
        self.target_placer = target_placer
        

    def run(self):
        output_dir = Path(self.settings.dataset.output_dir)
        output_dir.mkdir(parents = True, exist_ok = True)
        print(f"Output dir: {output_dir}")

        stage = self.stage_loader(self.scene_path)

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

            

            num_targets = random.randint(
                self.settings.dataset.min_targets_per_frame,
                self.settings.dataset.max_targets_per_frame,
            )
            targets = self.target_spawner.spawn(num_targets)
            self.target_placer.place(targets)



            with rep.trigger.on_frame(num_frames = self.settings.render.num_frames):
                pass


        self.orchestrator_runner(self.app)
        self.app.update()
        print("DatasetGenerator: Done.")