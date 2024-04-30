import glob
import os
from pathlib import Path

import click
from natsort import natsorted  # pyright: ignore

from .cbzmerge import ARCHIVE_EXTENSIONS, ComicMerge


@click.command()
@click.argument("output", type=str, nargs=1)
@click.option("--in", "-i", "input_glob", multiple=True,type=str, required=True, help=f"Input glob (relative to --folder). allowed extensions: {", ".join(ARCHIVE_EXTENSIONS)}. use -i='*.cbz' or w/e in powershell.")
@click.option("--folder", "-f", type=click.Path(file_okay=False, exists=True, dir_okay=True), default=os.getcwd(), help="Input folder for comics. If blank, uses current working directory of script.")
@click.option("--range", "-r", "range_", type=click.IntRange(), nargs=2, default=(0, -1), help="Range (start, end) (inclusive, 1-indexed) of comics in folder to merge")
@click.option("--chapters", "-c", is_flag=True, help="Don't flatten the directory tree, keep subfolders as chapters")
@click.option("--chunk-ch", "-cc", type=int, help="Autosplit into chunks by number of chapters. Only preserves chapter boundaries if --chapters is passed.")
@click.option("--chunk-mb", "-cm", type=int, help="Autosplit into chunks by max MB per chunk. Only preserves chapter boundaries if --chapters is passed.")
@click.option("--quieter", "-q", is_flag=True, help="Less information regarding the merging progress")
@click.version_option("1.0.0")
@click.help_option("-h", "--help")
def cli(
	input_glob: list[str] | str,
	output: str,
	folder: str,
	range_: tuple[int, int] | None,
	chunk_ch: int | None,
	chunk_mb: int | None,
	chapters: bool,
	quieter: bool, 
):
	comics_to_merge: list[str] = []
	folder = os.path.abspath(folder)
	print(folder, "in", input_glob, "out", output, "range", range_, "cc", chunk_ch, "cm", chunk_mb)

	# if input_glob:
	if isinstance(input_glob, str):
		input_glob = [ input_glob ]
	for pattern in input_glob:
		if pattern.startswith("="):
			pattern = pattern[1:]
		for file_path in natsorted(glob.glob(pattern, root_dir=folder)):
			if Path(file_path).suffix.lower() in ARCHIVE_EXTENSIONS:
				comics_to_merge.append(file_path)
	# else:
	# 	comics_to_merge = comics_in_folder(workdir=folder)

	if range_ is not None: # fallback to range
		start_idx = max(range_[0]-1, 0)
		end_idx = min(len(comics_to_merge), range_[1])
		if end_idx == -1:
			end_idx = len(comics_to_merge)
		comics_to_merge = comics_to_merge[start_idx:end_idx]

	if (len(comics_to_merge) == 0):
		print("Found no supported files for merging.")
		quit()

	comic_merge = ComicMerge(output, comics_to_merge, not quieter, chapters, workdir=folder)
	comic_merge.merge()

cli()
