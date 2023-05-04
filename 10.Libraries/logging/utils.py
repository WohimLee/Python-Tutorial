import os
from pathlib import Path


def mkdirs(path):
    try:
        os.makedirs(path)
    except Exception as e:
        ...

def mkparents(path):
    parents = Path(path).parent
    if not os.path.exists(parents):
        mkdirs(parents)
