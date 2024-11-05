import os.path
import importlib.resources

from typing import List

def get_spack_extension_paths() -> List[str]:
    dirname = importlib.resources.files("benchmark").parent
    if dirname.exists():  # type: ignore
        return [str(dirname)]
    return []

def get_spack_config_dir() -> str:
    return []
