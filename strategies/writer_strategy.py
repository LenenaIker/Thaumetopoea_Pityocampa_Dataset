from abc import ABC, abstractmethod

import omni.replicator.core as rep


class WriterStrategy(ABC):
    @abstractmethod
    def initialize(self, output_dir: str):
        raise NotImplementedError


class KittiWriterStrategy(WriterStrategy):
    def initialize(self, output_dir: str):
        writer = rep.WriterRegistry.get("KittiWriter")
        writer.initialize(output_dir=output_dir, omit_semantic_type=True)
        return writer
    
class CocoWriterStrategy(WriterStrategy):
    def initialize(self, output_dir: str):
        writer = rep.WriterRegistry.get("CocoWriter")
        writer.initialize(output_dir=output_dir, omit_semantic_type=True)
        return writer
    
class BasicRgbWriterStrategy(WriterStrategy):
    def initialize(self, output_dir: str):
        writer = rep.WriterRegistry.get("BasicWriter")
        writer.initialize(output_dir=output_dir, rgb=True)
        return writer
    
class BasicRgbBboxWriterStrategy(WriterStrategy):
    def initialize(self, output_dir: str):
        writer = rep.WriterRegistry.get("BasicWriter")
        writer.initialize(
            output_dir=output_dir,
            rgb=True,
            bounding_box_2d_tight=True,
            image_output_format="png"
        )
        return writer

class DebugBboxVisualizationWriterStrategy(WriterStrategy):
    def initialize(self, output_dir: str):
        writer = rep.WriterRegistry.get("DataVisualizationWriter")
        writer.initialize(
            output_dir=output_dir,
            bounding_box_2d_tight=True,
            bounding_box_2d_tight_params={
                "background": "rgb",
                "outline": "red",
                "fill": None,
                "width": 2,
            },
        )
        return writer


###### Null Writer ######
# Por si quiero ver ejecución sin guardar nada.
class NullWriter:
    def initialize(self, *args, **kwargs):
        return self

    def attach(self, *args, **kwargs):
        pass

class NullWriterStrategy(WriterStrategy):
    def initialize(self, output_dir: str):
        return NullWriter()