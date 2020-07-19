# Core Library modules
import logging
import os
import urllib.request
import zipfile
from os.path import expanduser
from typing import Any, Dict


def pytest_configure(config: Dict[Any, Any]) -> None:
    """Flake8 is to verbose. Mute it."""
    logging.getLogger("flake8").setLevel(logging.WARN)


lidtk_path = os.path.join(expanduser("~"), ".lidtk")

if not os.path.isdir(lidtk_path):
    print("Could not find ~/.lidtk - creating it")
    os.mkdir(lidtk_path)
    url = "https://zenodo.org/record/841984/files/wili-2018.zip"
    wili_zip_path = os.path.join(lidtk_path, "wili-2018.zip")

    print("Downloading wili dataset...")
    urllib.request.urlretrieve(url, wili_zip_path)

    wili_zip_path_target = os.path.join(lidtk_path, "data")
    print("Extracting wili dataset...")
    with zipfile.ZipFile(wili_zip_path, "r") as zip_ref:
        zip_ref.extractall(wili_zip_path_target)
    print("Downloaded and extracted wili dataset.")
