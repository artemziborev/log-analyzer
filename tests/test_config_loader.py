import os
import tempfile

import pytest

from src.app.services.config_loader import load_config


def test_load_config_merge() -> None:
    default = {"a": 1, "b": 2}
    yaml_text = "b: 99\nc: 3"
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write(yaml_text)
        path = f.name

    try:
        result = load_config(default, path)
        assert result["a"] == 1
        assert result["b"] == 99
        assert result["c"] == 3
    finally:
        os.remove(path)


def test_config_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        load_config({}, "nonexistent.yaml")
