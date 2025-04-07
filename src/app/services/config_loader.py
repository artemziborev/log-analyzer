import os

import yaml


def load_config(default: dict, path: str | None = None) -> dict:
    if not path:
        return default
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, encoding="utf-8") as f:
        try:
            custom = yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML: {e}")
    result = default.copy()
    result.update(custom)
    return result
