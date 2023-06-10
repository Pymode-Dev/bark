"""
This is the database manager module
"""

import sqlite3
from typing import Dict


class DatabaseManager:
    """
    Database Manager manages every action to be performed in a database.
    """

    def __init__(self, db_name: str) -> None:
        self.connection = sqlite3.connect(db_name)

    def _execute(self, statement: str, values=None) -> None:
        """
        This executes all sql statement passed into it.
        """
        cursor = self.connection.cursor()
        cursor.execute(statement, values or {})
        return cursor

    def create_table(self, table_name: str, data_schema: Dict) -> None:
        """
        Create a table if the table is not exists.
        """
        column_schema = [
            f"{column} {data_type}" for column, data_type in data_schema.items()
        ]
        self._execute(
            f"""
                CREATE TABLE IF NOT EXISTS {table_name}
                ({", ".join(column_schema)});
                """,
        )

    def insert_into_table(self, table_name: str, db_data: Dict) -> None:
        """
        Insert data into the database.
        """
        placeholders = [f"{column} = ?" for column in db_data.keys()]
        column_keys = ", ".join(db_data.keys())
        column_values = tuple(db_data.values())
        self._execute(
            f"""
                INSERT INTO {table_name}
                ({column_keys})
                VALUES ({placeholders});
                """,
            column_values,
        )

    def delete_from_table(self, table_name: str, bm_id: int) -> None:
        """
        Delete data from the table using id no.
        """
        self._execute(
            f"""
                DELETE FROM {table_name} WHERE id=?;
                """,
            bm_id,
        )

    def select_from_table(self, table_name: str, bm_id: int = None) -> None:
        """
        Read all data or read some selected data using id.
        """
        query = f"SELECT * FROM {table_name} "

        if bm_id:
            query += "WHERE id=?"
        query += " ORDER BY date_added;"

        return self._execute(query)

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Close and clean the database after being used.
        """
        if self.connection:
            self.connection.close()
