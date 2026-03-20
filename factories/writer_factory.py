from strategies.writer_strategy import (
    KittiWriterStrategy,
    CocoWriterStrategy,
    BasicRgbWriterStrategy,
)


class WriterFactory:
    def create(self, mode: str):
        if mode == "basic":
            return BasicRgbWriterStrategy()
        elif mode == "coco":
            return CocoWriterStrategy()
        elif mode == "kitti":
            return KittiWriterStrategy()
        else:
            raise ValueError(f"Unknown writer mode: {mode}")