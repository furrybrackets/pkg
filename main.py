usage = """
pkg

Usage:
  pkg -h | --help
  pkg -v | --version

Options:
  -h --help     Show this screen.
  -v --version     Show the current version.
"""
from docopt import docopt

args=docopt(usage)

if args["--version"] == True:
  print("pkg version 0.1)
