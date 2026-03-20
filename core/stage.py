from omni.isaac.core.utils.stage import open_stage, get_current_stage

def load_stage(stage_path: str):
    print(f"Loading stage: {stage_path}")
    open_stage(stage_path)
    stage = get_current_stage()
    if stage is None:
        raise RuntimeError(f"Could not open stage: {stage_path}")
    return stage