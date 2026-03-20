from strategies.camera_strategy import (
    FixedCameraStrategy,
    DroneCameraStrategy,
    RandomCameraStrategy,
)


class CameraFactory:
    def create(self, mode: str):
        if mode == "drone":
            return DroneCameraStrategy()
        elif mode == "random":
            return RandomCameraStrategy()
        elif mode == "fixed":
            return FixedCameraStrategy()
        else:
            raise ValueError(f"Unknown camera mode: {mode}")