import sys
from pathlib import Path

from .mkposter import mkposter


_, filename = sys.argv
mkposter(Path(filename))
