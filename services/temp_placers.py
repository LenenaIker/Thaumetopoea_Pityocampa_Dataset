import math
import omni.replicator.core as rep # pyright: ignore[reportMissingImports]
import random

class RingTargetPlacer:
    def __init__(self, center=(0, 0, 3), radius=2.5, scale=(0.5, 0.5, 0.5)):
        self.center = center
        self.radius = radius
        self.scale = scale

    def place(self, targets):
        cx, cy, cz = self.center
        n = len(targets)

        if n == 1:
            with targets[0]:
                rep.modify.pose(
                    position=(cx, cy, cz),
                    scale=self.scale,
                )
            return

        for i, target in enumerate(targets):
            angle = (2 * math.pi * i) / n
            x = cx + self.radius * math.cos(angle)
            y = cy + self.radius * math.sin(angle)

            with target:
                rep.modify.pose(
                    position=(x, y, cz),
                    scale=self.scale,
                )


ZONES = {
    "center": (0, 0, 3),
    "north": (0, 2, 3),
    "south": (0, -2, 3),
    "east": (2, 0, 3),
    "west": (-2, 0, 3),
}

class DiscreteZonePlacer:
    def __init__(self, zones = ZONES, scale=(0.5, 0.5, 0.5)):
        self.zones = zones
        self.scale = scale

    def place(self, targets):
        zone_keys = list(self.zones.keys())

        for target in targets:
            zone = random.choice(zone_keys)
            pos = self.zones[zone]

            with target:
                rep.modify.pose(
                    position=pos,
                    scale=self.scale,
                )