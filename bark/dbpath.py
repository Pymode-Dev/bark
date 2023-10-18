"""
check_os_version.py
"""
from pathlib import Path


def create_database_path() -> Path:
    """
    create_database_path: This create the folder where the database file will be saved
    Args:
        None
    Return:
        str
    """
    app_dir = Path.home() / "bark"
    app_dir.mkdir(exist_ok=True)
    return app_dir
