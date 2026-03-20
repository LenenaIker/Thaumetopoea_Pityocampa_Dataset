from abc import ABC, abstractmethod
import omni.replicator.core as rep

class CameraStrategy(ABC):
    @abstractmethod
    def create_camera(self):
        raise NotImplementedError


class FixedCameraStrategy(CameraStrategy):
    def create_camera(self):
        return rep.create.camera(
            position=(0, -12, 6),
            look_at=(0, 0, 3),
            clipping_range=(0.1, 10000),
        )
    
class RandomCameraStrategy(CameraStrategy):
    def create_camera(self):
        cam = rep.create.camera()
        with cam:
            rep.modify.pose(
                position=rep.distribution.uniform((-10, -10, 2), (10, 10, 5)),
                look_at=(0, 0, 2),
            )
        return cam


class DroneCameraStrategy(CameraStrategy):
    def create_camera(self):
        return rep.create.camera(position=(0, -20, 10), look_at=(0, 0, 5))