import sqlite3
import os


class Database:

    def __init__(self):

        os.makedirs("data", exist_ok=True)

        self.connection = sqlite3.connect("data/leadgen.db")

        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):

        self.cursor.execute(query, params)

        self.connection.commit()

    def fetchall(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchall()

    def fetchone(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchone()

    def close(self):

        self.connection.close()