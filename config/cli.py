import argparse
import os

def parse_args():

    parser = argparse.ArgumentParser("Dataset generator")
    parser.add_argument("--headless", type=bool, default=False, help="Launch script headless, default is False")
    parser.add_argument("--height", type=int, default=544, help="Height of image")
    parser.add_argument("--width", type=int, default=960, help="Width of image")
    parser.add_argument("--num_frames", type=int, default=1000, help="Number of frames to record")
    # parser.add_argument("--distractors", type=str, default="warehouse", help="Options are 'warehouse' (default), 'additional' or None")
    parser.add_argument("--data_dir", type=str, default=os.getcwd() + "/_tp_nest_data", help="Location where data will be output")
    parser.add_argument("--camera_mode", type=str, default="fixed")
    parser.add_argument("--writer_type", type=str, default="none")
    parser.add_argument("--warmup_steps", type=int, default=100)
    parser.add_argument("--rt_subframes", type=int, default=1)
    parser.add_argument("--renderer", type=str, default="RayTracedLighting")

    args, unknown_args = parser.parse_known_args()

    print("Unknown args:\n", unknown_args)

    return args
