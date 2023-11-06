# This script generates the different versions of the ansys-dpf-core wheels based on a given input.
# Input can be one of ["any", "win", "manylinux1", "manylinux_2_17"]

import argparse
import subprocess
import os
import sys
import shutil
import tempfile


supported_platforms = {
    "any": "any",
    "win": "win_amd64",
    "manylinux1": "manylinux1_x86_64",
    "manylinux_2_17": "manylinux_2_17_x86_64",
}

argParser = argparse.ArgumentParser()
argParser.add_argument("-p", "--platform", help="platform")
argParser.add_argument("-w", "--wheelhouse", help="platform", action="store_true")

args = argParser.parse_args()

if args.platform not in supported_platforms:
    raise ValueError(
        f"Platform {args.platform} is not supported. "
        f"Supported platforms are: {list(supported_platforms.keys())}"
    )
else:
    requested_platform = supported_platforms[args.platform]
print(requested_platform)

# Move binaries out of the source depending on platform requested
# any: move all binaries out before building
# win: move .so binaries out before building
# lin: move .dll binaries out before building
with tempfile.TemporaryDirectory() as tmpdirname:
    print("Created temporary directory: ", tmpdirname)

    # Create the temporary build-opts.cfg
    build_opts_path = os.path.join(tmpdirname, "build-opts.cfg")
    with open(build_opts_path, "w") as build_opts_file:
        build_opts_file.write(f"[bdist_wheel]\nplat-name={requested_platform}")
    os.environ["DIST_EXTRA_CONFIG"] = build_opts_path

    # Move the binaries
    gatebin_folder_path = os.path.join(
        os.path.curdir, os.path.join("src", "ansys", "dpf", "gatebin")
    )
    binaries_to_move = []
    moved = []
    if "win" in requested_platform or "any" == requested_platform:
        # Move linux binaries
        binaries_to_move.extend(["libAns.Dpf.GrpcClient.so", "libDPFClientAPI.so"])
    if "linux" in requested_platform or "any" == requested_platform:
        # Move windows binaries
        binaries_to_move.extend(["Ans.Dpf.GrpcClient.dll", "DPFClientAPI.dll"])
    if "any" == requested_platform:
        binaries_to_move.extend(["_version.py"])

    for binary_name in binaries_to_move:
        src = os.path.join(gatebin_folder_path, binary_name)
        dst = os.path.join(tmpdirname, binary_name)
        print(f"Moving {src} to {dst}")
        shutil.move(src=src, dst=dst)
        moved.append([dst, src])

    if "any" == requested_platform:
        # Also remove the gatebin folder
        os.rmdir(gatebin_folder_path)

    # Call the build
    if not args.wheelhouse:
        cmd = [sys.executable, "-m", "build", "--wheel"]
    else:
        cmd = [sys.executable, "-m", "pip", "wheel", "-w", "dist", "."]
    try:
        subprocess.run(cmd, capture_output=False, text=True)
        print("Done building the wheel.")
    except Exception as e:
        print(f"Build failed with error: {e}")

    if "any" == requested_platform:
        # Recreate the gatebin folder
        os.mkdir(gatebin_folder_path)

    # Move binaries back
    for move_back in moved:
        print(f"Moving back {move_back[0]} to {move_back[1]}")
        shutil.move(src=move_back[0], dst=move_back[1])
    print("Binaries moved back.")

    print(f"Done building {requested_platform} wheel for ansys-dpf-core!")
