
from omni.isaac.kit import SimulationApp
import os
import argparse

parser = argparse.ArgumentParser("Dataset generator")
parser.add_argument("--headless", type=bool, default=False, help="Launch script headless, default is False")
parser.add_argument("--height", type=int, default=544, help="Height of image")
parser.add_argument("--width", type=int, default=960, help="Width of image")
parser.add_argument("--num_frames", type=int, default=1000, help="Number of frames to record")
# parser.add_argument("--distractors", type=str, default="warehouse", help="Options are 'warehouse' (default), 'additional' or None")
parser.add_argument("--data_dir", type=str, default=os.getcwd() + "/_tp_nest_data", help="Location where data will be output")

args, unknown_args = parser.parse_known_args()


CONFIG = {
    "renderer": "RayTracedLighting",
    "headless": args.headless,
    "width": args.width,
    "height": args.height,
    "num_frames": args.num_frames
}

simulation_app = SimulationApp(launch_config=CONFIG)


## This is the path which has the background scene in which objects will be added.
ENV_URL = "/Isaac/Environments/_"

import carb
import omni
import omni.usd
from omni.isaac.core.utils.nucleus import get_assets_root_path
from omni.isaac.core.utils.stage import get_current_stage, open_stage
from pxr import Semantics
import omni.replicator.core as rep

from omni.isaac.core.utils.semantics import get_semantics

# Increase subframes if shadows/ghosting appears of moving objects
# See known issues: https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_replicator.html#known-issues
rep.settings.carb_settings("/omni/replicator/RTSubframes", 4)


PINES = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Yellow_Pine.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Douglas_Fir.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Eastern_Hemlock.usd"
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Norway_Spruce.usd"
]
SMALL_PINES = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Colorado_Spruce.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/White_Pine.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Italian_Cypress.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Chinese_Juniper.usd"
]
OTHER_TREES = [

]
NESTS = []
ENV_OBJECTS = [] # Harriak, sasiak, enborrak, ¿beste zuhaitzak?
DISTRACTORS = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/Props/Shapes/sphere.usd",
    
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Debris/maplefall1.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Debris/oakfall1.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Debris/oakfall2.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Food/Fruit/Apple.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Entertainment/Games/Ball_Walnut.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Food/Fruit/Avocado01.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Decor/Tchotchkes/Orange_01.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Decor/Tchotchkes/Orange_02.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Decor/Tchotchkes/Orange_03.usd"
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Food/Vegetables/RedOnion.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Decor/Sculptures/SpeakNoEvil_Skull.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Entertainment/Games/Solid_Marble.usd"
] # Piñuak, plastiko boltsak, txoriak, txori kabiak,

TRASH = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/DigitalTwin/Assets/Warehouse/Storage/Bottles/Plastic/NaturalBostonRound_A/NaturalBostonRoundBottle_A01_PR_NVD_01.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/DigitalTwin/Assets/Warehouse/Storage/Bottles/Plastic/NaturalBostonRound_A/NaturalBostonRoundBottle_A02_PR_NVD_01.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/DigitalTwin/Assets/Warehouse/Storage/Bottles/Plastic/NaturalBostonRound_A/NaturalBostonRoundBottle_A03_PR_NVD_01.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Food/Containers/TinCan.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/DigitalTwin/Assets/Warehouse/Storage/Jugs/Plastic_Jerrican_A/PlasticJerrican_A01_PR_V_NVD_01.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/DigitalTwin/Assets/Warehouse/Storage/Jugs/Plastic_Jerrican_A/PlasticJerrican_A02_PR_V_NVD_01.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/DigitalTwin/Assets/Warehouse/Storage/Jugs/Plastic_Jerrican_A/PlasticJerrican_A03_PR_V_NVD_01.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/DigitalTwin/Assets/Warehouse/Storage/Jugs/Plastic_Jerrican_A/PlasticJerrican_A04_PR_V_NVD_01.usd"
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Kitchen/Kitchenware/StorageAndOrganization/paper_towel.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Kitchen/Kitchenware/Dinnerware/P_Glassware_Short.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Kitchen/Kitchenware/Dinnerware/P_Glassware_Tall.usd"
]

BUSHES = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Shrub/Switchgrass.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Shrub/Pampas_Grass.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Shrub/Fountain_Grass_Short.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Shrub/Fountain_Grass_Tall.usd"
]

GRASS = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Shrub/Grass_Short_A.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Shrub/Grass_Short_B.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Shrub/Grass_Short_C.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Shrub/Grass_Trimmed_A.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Shrub/Grass_Trimmed_B.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Shrub/Grass_Trimmed_C.usd"
]


# TODO: Distractor talde bakarra o zuhaitzentzat bat ta lurreako beste bat?
TEXTURES = []



def main():
    pass


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        carb.log_error(f"Exception: {e}")
        import traceback

        traceback.print_exc()
    finally:
        simulation_app.close()
