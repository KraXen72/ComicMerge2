import click

# from .cbzmerge import ComicMerge, comics_from_indices, comics_from_prefix, comics_in_folder

# parser = argparse.ArgumentParser(prog="ComicMerge", description="Merge multiple cbz files into one.")
# parser.add_argument("-f", "--folder", type=str, help="Input folder for comics. If blank, uses current working directory of script.")
# # parser.add_argument("-m", "--max", type=int, help="Max size for output file in MB. produces multiple chunk files if over limit")
# parser.add_argument(
# 	"output_name", metavar="OUTPUT_FILE", type=str, help="Name of the .cbz file to be created. Will automatically append .cbz if necessary."
# )
# parser.add_argument("-v", "--verbose", action="store_true", help="More information as to the merging progress")
# parser.add_argument("-p", "--prefix", type=str, help="Prefix to restrict comics to")
# parser.add_argument(
# 	"-r",
# 	"--range",
# 	nargs=2,
# 	metavar=("start", "end"),
# 	type=int,
# 	help="Specified by the format X Y. Only the Xth to Yth comic in the folder will be merged into the " "output file.",
# )
# parser.add_argument("-c", "--chapters", action="store_true", help="Don't flatten the directory tree, keep subfolders as chapters")
# parser.add_argument("--cbr", action="store_true", help="Look for .cbr files instead of .cbz")

# args = parser.parse_args()

# workdir = args.folder
# if workdir is None:
# 	workdir = "."

# if args.prefix is not None:  # prefix is king
# 	comics_to_merge = comics_from_prefix(args.prefix, args.cbr, workdir=workdir)
# elif args.range is not None:  # fallback to range
# 	if (len(args.range)) == 0:
# 		comics_to_merge = comics_from_indices(0, -1, args.cbr, workdir=workdir)
# 	else:
# 		comics_to_merge = comics_from_indices(args.range[0], args.range[1], args.cbr, workdir=workdir)
# else:  # no range = all comics in folder
# 	comics_to_merge = comics_in_folder(args.cbr, workdir=workdir)

# if (len(comics_to_merge) == 0):
# 	print("Found no cbz files for merging. use flag --cbr to look for .cbr files")
# 	quit()


@click.command()
@click.argument("output", type=str, required=True, nargs=1)
@click.option("--folder", "-f", type=click.Path(file_okay=False, exists=True, dir_okay=True), help="Input folder for comics. If blank, uses current working directory of script.")
@click.option("--prefix", "-p", type=str, help="Filename prefix filter to restrict input comics")
@click.option("--range", "-r", type=click.IntRange(min=1, clamp=True), nargs=2, help="Range of comics in folder to merge", )
@click.option("--chapters", "-c", is_flag=True, help="Don't flatten the directory tree, keep subfolders as chapters")
@click.option("--cbr", is_flag=True, help="Look for .cbr files instead of .cbz")
@click.option("--verbose", "-v", is_flag=True, help="More information as to the merging progress")
@click.help_option("-h", "--help")
def cli(
	output: str,
	prefix: str,
	comic_range: click.IntRange,
	chapters: bool,
	cbr: bool,
	verbose: bool, 
	folder = ".",
	# comics_to_merge, 
	# verbose,
	# chapters, 
	# cbr, 
	# workdir
):
	print(output, folder, prefix, comic_range, chapters, cbr, verbose)
	# comic_merge = ComicMerge(args.output_name, comics_to_merge, args.verbose, args.chapters, args.cbr, workdir=args.folder)
	# comic_merge.merge()
