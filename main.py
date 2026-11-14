"""food-picture-01 entry: emit one food picture (tonkotsu noodle-pull iteration).

Stdlib only, no network, deterministic: the program copies the exact bytes
of entry.png beside it to $MAKEFUN_OUTPUT_DIR/entry.png on every run.

Gate constraints (verified): the image is a whole PNG of 822,904 bytes
(at most 1 MiB) and 784 by 784 pixels (at most 1024 by 1024). The picture
follows the board-proven formula: a tall noodle pull, a jammy egg with its
yolk dripping into the broth, chashu, chili-oil swirl, steam, moody bokeh.
"""

import os
import shutil

IMAGE_NAME = "entry.png"


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGE_NAME)
    shutil.copyfile(src, os.path.join(outdir, IMAGE_NAME))


if __name__ == "__main__":
    main()
