import omni.replicator.core as rep
from pathlib import Path
from config.settings import Settings

class DatasetGenerator:
    def __init__(
        self,
        app,
        settings: Settings,
        scene_path,
        camera_strategy,
        writer_strategy,
        orchestrator_runner,
        stage_loader
    ):
        self.app = app
        self.settings = settings
        self.scene_path = scene_path

        self.camera_strategy = camera_strategy
        self.writer_strategy = writer_strategy
        self.orchestrator_runner = orchestrator_runner
        self.stage_loader = stage_loader

    def run(self):
        output_dir = Path(self.settings.dataset.output_dir)
        output_dir.mkdir(parents = True, exist_ok = True)
        print(f"Output dir: {output_dir}")

        stage = self.stage_loader(self.scene_path)

        for _ in range(self.settings.dataset.warmup_steps):
            self.app.update()


        with rep.new_layer():

            camera = self.camera_strategy.create_camera()

            render_product = rep.create.render_product(
                camera,
                (self.settings.render.width, self.settings.render.height)
            )

            writer = self.writer_strategy.initialize(
                str(self.settings.dataset.output_dir)
            )
            writer.attach([render_product])



            target = rep.create.from_usd(
                "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/Props/Shapes/sphere.usd",
                semantics=[("class", self.settings.dataset.target_class)],
                count=1
            )

            # Posición fija visible
            with target:
                rep.modify.pose(
                    position=(0, 0, 3),
                    scale=(0.5, 0.5, 0.5)
                )


            with rep.trigger.on_frame(num_frames=self.settings.render.num_frames):
                pass


        self.orchestrator_runner(self.app)
        self.app.update()
        print("DatasetGenerator: Done.")