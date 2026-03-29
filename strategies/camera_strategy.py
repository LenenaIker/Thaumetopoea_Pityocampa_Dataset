from abc import ABC, abstractmethod
import omni.replicator.core as rep # pyright: ignore[reportMissingImports]

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

# TODO: Esto no debe de ser un strategy y CameraFactory no debe de existir --> Overengineering. Kamara zuzenean Generatorren sortu!

# TODO: rep.create.stereo_camera() --> Teniendo en cuenta que el dron va a tener que medir profundidad...


# class RandomCameraStrategy(CameraStrategy):
#     def create_camera(self):
#         cam = rep.create.camera()

#         with cam:
#             rep.modify.pose(
#                 position = rep.distribution.uniform(
#                     (-20, -20, 2),
#                     (20, 20, 12)
#                 ),
#                 look_at = rep.distribution.uniform(
#                     (-5, -5, 0),
#                     (5, 5, 5)
#                 ),
#             )
#         return cam


# class DroneCameraStrategy(CameraStrategy):
#     def create_camera(self):
#         cam = rep.create.camera()
#         with cam:
#             rep.modify.pose(
#                 position = rep.distribution.uniform(
#                     (-30, -30, 8),
#                     (30, 30, 20)
#                 ),
#                 look_at = rep.distribution.uniform(
#                     (-5, -5, 0),
#                     (5, 5, 8)
#                 ),
#             )
#         return cam

