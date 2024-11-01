from . import *
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", type=int, default=5678, help="Debugpy endpoint")
    parser.add_argument("--filename", default="checkpoint.dump", help="Dumpfile name")
    args = parser.parse_args()
    launch_debug_server(args.filename, args.endpoint)