
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
ASSETS_DIR = PROJECT_ROOT / "assets"
SCENES_DIR = ASSETS_DIR / "scenes"


FOREST_01 = str((SCENES_DIR / "forest_01.usd").resolve())
NEST_01 = str((ASSETS_DIR / "Nest.usd").resolve())


PINES = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Yellow_Pine.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Douglas_Fir.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Eastern_Hemlock.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Norway_Spruce.usd"
]

SMALL_PINES = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Colorado_Spruce.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/White_Pine.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Italian_Cypress.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Chinese_Juniper.usd"
]

OTHER_PLUS_6M_TREES = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/American_Beech.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Black_Oak.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Black_Oak_Fall.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Common_Apple.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Hawthorn.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Honey_Locust.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Honey_Locust_Fall.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Largetooth_Aspen.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Lombardy_Poplar.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Lombardy_Poplar_Fall.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Red_Ash.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Red_Ash_Fall.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Red_Maple.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Red_Oak.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Scarlet_Oak.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Scarlet_Oak_fall.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Service_Berry.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Shumard_Oak.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Shumard_Oak_Fall.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Siberian_Crab_Apple.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Sugar_Maple.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/Sycamore.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Trees/White_Ash.usd"
]

NESTS = [
    NEST_01
]
TEMP_NESTS = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/5.1/Isaac/Props/Shapes/sphere.usd",
    # "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Decor/Sculptures/SpeakNoEvil_Skull.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Entertainment/Games/Solid_Marble.usd"
]

NEST_DISTRACTORS = [
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Debris/maplefall1.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Debris/oakfall1.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Vegetation/Debris/oakfall2.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Food/Fruit/Apple.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Entertainment/Games/Ball_Walnut.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Food/Fruit/Avocado01.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Decor/Tchotchkes/Orange_01.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Decor/Tchotchkes/Orange_02.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Decor/Tchotchkes/Orange_03.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/ArchVis/Residential/Food/Vegetables/RedOnion.usd"
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

ENV_OBJECTS = [

] # Harriak, sasiak, enborrak

DISTRACTORS = [
    *OTHER_PLUS_6M_TREES,
    *BUSHES,
    *GRASS,
]

# TODO: Distractor talde bakarra o zuhaitzentzat bat ta lurreako beste bat?
TEXTURES = []


