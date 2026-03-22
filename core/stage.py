from pathlib import Path
from isaacsim.core.utils.stage import open_stage, get_current_stage

def load_stage(stage_path: str | Path): # Dokumentazioan: str | Path | usdrt.Sdf.Path
    print(f"Loading stage: {stage_path}")
    open_stage(stage_path)
    stage = get_current_stage()
    if stage is None:
        raise RuntimeError(f"Could not open stage: {stage_path}")
    return stage