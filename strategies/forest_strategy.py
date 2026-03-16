from abc import ABC, abstractmethod


class RandomizationStrategy(ABC):
    @abstractmethod
    def apply(self, context) -> None:
        pass


class ForestRandomizationStrategy(RandomizationStrategy):
    def apply(self, context) -> None:
        context.randomize_camera()
        context.randomize_targets()
        context.randomize_distractors()
        context.randomize_lighting()
        context.randomize_materials()
