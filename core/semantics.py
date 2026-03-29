from pxr import Semantics # pyright: ignore[reportMissingImports]


def update_semantics(stage, keep_semantics=None):
    """Remove semantics from the stage except for keep_semantic classes."""
    keep_semantics = set(keep_semantics or [])

    for prim in stage.Traverse():
        if prim.HasAPI(Semantics.SemanticsAPI):
            processed_instances = set()

            for property in prim.GetProperties():
                is_semantic = Semantics.SemanticsAPI.IsSemanticsAPIPath(property.GetPath())
                if not is_semantic:
                    continue

                instance_name = property.SplitName()[1]

                if instance_name in processed_instances:
                    # Skip repeated instance, instances are iterated twice due to
                    # their two semantic properties (class, data)
                    continue

                processed_instances.add(instance_name)
                sem = Semantics.SemanticsAPI.Get(prim, instance_name)
                type_attr = sem.GetSemanticTypeAttr()
                data_attr = sem.GetSemanticDataAttr()

                if data_attr.Get() not in keep_semantics:
                    prim.RemoveProperty(type_attr.GetName())
                    prim.RemoveProperty(data_attr.GetName())
                    prim.RemoveAPI(Semantics.SemanticsAPI, instance_name)