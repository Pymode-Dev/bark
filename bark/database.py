"""
database.py
"""

from pathlib import Path
from typing import Dict, List

from tinydb import Query, TinyDB


class DatabaseManager:
    """
    class:
        DatabaseManager: This manages all database operation
    Methods:
        insert_bookmark: store a bookmark
        delete_bookmark: remove a bookmark from the database
        read_bookmark: read what you store
        update_bookmark: update your bookmark
    """

    def __init__(self, db_name: Path) -> None:
        self.db_name = TinyDB(f"{db_name}.json")

    def insert_bookmark(self, bk_data: Dict) -> int:
        """
        insert_bookmark: store a bookmark
        Args:
            bk_data: dict - the bookmark to store
        Return:
            int: The bookmark ID store
        """
        return self.db_name.insert(bk_data)

    def delete_bookmark(self, bk_title: str) -> None:
        """
        delete_bookmark: remove a bookmark using the title of the bookmark
        Args:
            bk_title: str = the title to use
        Return:
            None
        """
        query = Query()

        return self.db_name.remove(query.title == bk_title)

    def read_bookmark(self, bk_title=None) -> List:
        """
        read_bookmark: read all your bookmark or a specific one
        Args:
            bk_title: str - if specify by the user
        Return:
            list: if the bookmark is found or else it returns []
        """
        query = Query()

        if bk_title:
            return self.db_name.search(query.title == bk_title)
        return self.db_name.all()

    def update_bookmark(self, bk_data: dict, bk_title: str) -> None:
        """
        update_bookmark: update a bookmark using the title to found the exact bookmark
        Args:
            bk_data: dict - the data to replace in place of the old one
            bk_title: str - the condition key to find the specific bookmark
        Return:
            None
        """
        query = Query()

        return self.db_name.update(bk_data, query.title == bk_title)
