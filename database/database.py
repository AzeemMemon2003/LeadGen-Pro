import sqlite3

from config.settings import Settings


class Database:

    def __init__(self):

        Settings.create_directories()

        self.connection = sqlite3.connect(
            Settings.DATABASE,
            check_same_thread=False
        )

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):

        self.cursor.execute(query, params)

        self.connection.commit()

    def executemany(self, query, params):

        self.cursor.executemany(query, params)

        self.connection.commit()

    def fetchall(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchall()

    def fetchone(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchone()

    def close(self):

        self.connection.close()