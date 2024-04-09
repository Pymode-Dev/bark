"""
commands.py
"""
import datetime as dt
import sys

from .database import DatabaseManager
from .dbpath import create_database_path

db_path = create_database_path() / "bookmark"
db_instance = DatabaseManager(db_path)


class InsertBookmark:
    """
    class:
        InsertBookmark
    """

    def execute(self, data: dict) -> str:
        """
        execute: execute the command
        Args:
            data: dict - the data to operate on
        Return:
            str
        """
        data["date_added"] = dt.datetime.now().strftime("%d %b, %Y %H:%M:%S")
        output = db_instance.insert_bookmark(data)
        if isinstance(output, int):
            return "Bookmark inserted successfully"
        return "Insertion failed."


class DeleteBookmark:
    """
    class:
        DeleteBookmark
    """

    def execute(self, data: str) -> str:
        """
        execute: execute the command
        Args:
            data: dict - the data to operate on
        Return:
                str:
        """
        db_instance.delete_bookmark(data)
        return "Bookmark deleted successfully"


class ReadBookmark:
    """
    class:
        ReadBookmark
    """

    def execute(self, data=None) -> list:
        """
        execute: execute the command
        Args:
            data: if available
        Return:
            list
        """
        db_output = None
        if data:
            db_output = db_instance.read_bookmark(data)
        else:
            db_output = db_instance.read_bookmark()
        return db_output


class UpdateBookmark:
    """
    class:
        UpdateBookmark
    """

    def execute(self, data: dict) -> str:
        """
        execute: execute the command
        Args:
            data: dict - the data to replace the old one
            param: str - the key to find the bookmark to update
        Return:
            str
        """
        param = data['title']
        data["date_added"] = dt.datetime.now().strftime("%d %b, %Y %H:%M:%S")
        db_instance.update_bookmark(data, param)
        return "Bookmark updated successfully."


class Quit:
    """
    class:
        Quit: quit the entire app when called
    """

    def execute(self):
        """
        execute: execute what the class meant for.
        Args:
            None
        Return:
            None
        """
        sys.exit()
