from pathlib import Path
import shutil

from PIL import Image, ImageDraw


SIZES = [8, 16, 32, 64, 128, 256, 512]
WIDTH = 4

# Colors
TRANSPARENT = (0, 0, 0, 0)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)


output_dir = Path("./assets")
if output_dir.is_dir():
    shutil.rmtree(output_dir)
output_dir.mkdir()

# Squares
squares_dir = output_dir / "squares"
squares_dir.mkdir()
for w_index in range(len(SIZES)):
    width = SIZES[w_index]
    for h_index in range(-1, -len(SIZES) + w_index - 1, -1):
        height = SIZES[h_index]

        im = Image.new(mode="RGBA", size=(width, height), color=TRANSPARENT)
        draw = ImageDraw.Draw(im)
        draw.rectangle(
            [(0, 0), (width - 1, height - 1)],
            fill=BLACK,
            outline=WHITE,
            width=WIDTH,
        )
        im.save(squares_dir / f"sq_{width}x{height}.png")


# Triangles
triangles_dir = output_dir / "triangles"
triangles_dir.mkdir()
for w_index in range(len(SIZES)):
    width = SIZES[w_index]
    for h_index in range(-1, -len(SIZES) + w_index - 1, -1):
        height = SIZES[h_index]

        # symetric
        im = Image.new(mode="RGBA", size=(width, height), color=TRANSPARENT)
        draw = ImageDraw.Draw(im)
        draw.polygon(
            [
                (width // 2 - 1, 0),
                (width - 1, height - 1),
                (0, height - 1),
                (width // 2 - 1, 0),
            ],
            fill=BLACK,
            outline=WHITE,
            width=WIDTH,
        )
        im.save(triangles_dir / f"tri_{width}x{height}.png")

# Slops
slops_dir = output_dir / "slops"
slops_dir.mkdir()
for w_index in range(len(SIZES)):
    width = SIZES[w_index]
    for h_index in range(-1, -len(SIZES) + w_index - 1, -1):
        height = SIZES[h_index]

        # half
        im = Image.new(mode="RGBA", size=(width, height), color=TRANSPARENT)
        draw = ImageDraw.Draw(im)
        draw.polygon(
            [(0, 0), (width - 1, 0), (0, height - 1), (0, 0)],
            fill=BLACK,
            outline=WHITE,
            width=WIDTH,
        )
        im.save(slops_dir / f"slop_{width}x{height}.png")

# Circles
circles_dir = output_dir / "circles"
circles_dir.mkdir()
for width in SIZES:
    # half
    im = Image.new(mode="RGBA", size=(width, width), color=TRANSPARENT)
    draw = ImageDraw.Draw(im)
    draw.ellipse(
        [(0, 0), (width - 1, width - 1)],
        fill=BLACK,
        outline=WHITE,
        width=WIDTH,
    )
    im.save(circles_dir / f"circ_{width}x{height}.png")
