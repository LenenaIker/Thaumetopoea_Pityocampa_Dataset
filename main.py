
from omni.isaac.kit import SimulationApp

from config.cli import parse_args
from config.settings import build_settings


def main():
    settings = build_settings(args = parse_args())

    app = SimulationApp(launch_config = settings.to_launch_config())

    try:
        # Hemen ezbaet jartzen errorea emateia omni liburutegiak erabiltzeagatik SimulationApp-en aurretk
        from scenarios.forest_base import build_forest_base_generator

        generator = build_forest_base_generator(settings = settings, app = app)
        generator.run()
    finally:
        app.close()


if __name__ == "__main__":
    main()

