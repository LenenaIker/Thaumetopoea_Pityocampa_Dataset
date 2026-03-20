from strategies.writer_strategy import (
    KittiWriterStrategy,
    CocoWriterStrategy,
    BasicRgbWriterStrategy,
    BasicRgbBboxWriterStrategy,
    NullWriterStrategy,
    DebugBboxVisualizationWriterStrategy
)


class WriterFactory:
    _registry = {
        "basic": BasicRgbWriterStrategy,
        "basic_bbox": BasicRgbBboxWriterStrategy,
        "debug_bbox": DebugBboxVisualizationWriterStrategy,
        "coco": CocoWriterStrategy,
        "kitti": KittiWriterStrategy,
        "none": NullWriterStrategy,

    }
    
    def create(self, mode: str):
        try:
            return self._registry[mode.lower()]()
        except KeyError:
            raise ValueError(f"Unknown writer mode: {mode}")