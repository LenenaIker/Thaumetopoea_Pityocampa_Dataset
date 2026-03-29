from strategies.camera_strategy import (
    FixedCameraStrategy,
    # DroneCameraStrategy,
    # RandomCameraStrategy,
)

class CameraFactory:
    _registry = {
        "fixed": FixedCameraStrategy,
        # "random": RandomCameraStrategy,
        # "drone": DroneCameraStrategy,
    }

    def create(self, mode: str):
        try:
            return self._registry[mode.lower()]()
        except KeyError:
            raise ValueError(f"Unknown camera mode: {mode}")