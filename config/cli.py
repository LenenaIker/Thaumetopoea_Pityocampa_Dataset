import argparse


def parse_args():
    parser = argparse.ArgumentParser("Dataset generator")

    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--height", type=int)
    parser.add_argument("--width", type=int)
    parser.add_argument("--num_frames", type=int)
    parser.add_argument("--data_dir", type=str)
    parser.add_argument("--camera_mode", type=str)
    parser.add_argument("--writer_type", type=str)
    parser.add_argument("--warmup_steps", type=int)
    parser.add_argument("--rt_subframes", type=int)
    parser.add_argument("--renderer", type=str)
    parser.add_argument("--target_class", type=str)
    parser.add_argument("--distractor_type", type=str)

    args, unknown_args = parser.parse_known_args()
    print("Unknown args:\n", unknown_args)
    return args