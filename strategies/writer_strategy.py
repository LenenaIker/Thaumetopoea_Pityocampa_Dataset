from abc import ABC, abstractmethod
from pathlib import Path


class WriterStrategy(ABC):
    @abstractmethod
    def initialize(self, rep, output_dir: Path):
        pass


class KittiWriterStrategy(WriterStrategy):
    def initialize(self, rep, output_dir: Path):
        writer = rep.WriterRegistry.get("KittiWriter")
        writer.initialize(output_dir=str(output_dir), omit_semantic_type=True)
        return writer
    
class CocoWriterStrategy(WriterStrategy):
    def initialize(self, rep, output_dir: Path):
        writer = rep.WriterRegistry.get("CocoWriter")
        writer.initialize(output_dir=str(output_dir), omit_semantic_type=True)
        return writer