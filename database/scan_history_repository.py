from datetime import datetime

from database.database import Database
from database.models import SCAN_HISTORY_TABLE


class ScanHistoryRepository:

    def __init__(self):

        self.db = Database()

        self.db.execute(
            SCAN_HISTORY_TABLE
        )

    def start_scan(self, total_websites):

        created = datetime.now().isoformat()

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            INSERT INTO scan_history
            (
                started_at,
                total_websites,
                successful,
                failed,
                duration_seconds,
                status,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                created,
                total_websites,
                0,
                0,
                0,
                "RUNNING",
                created
            )
        )

        self.db.connection.commit()

        return cursor.lastrowid

    def finish_scan(
        self,
        scan_id,
        successful,
        failed,
        duration_seconds
    ):

        finished = datetime.now().isoformat()

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            UPDATE scan_history
            SET
                finished_at = ?,
                successful = ?,
                failed = ?,
                duration_seconds = ?,
                status = ?
            WHERE id = ?
            """,
            (
                finished,
                successful,
                failed,
                duration_seconds,
                "COMPLETED",
                scan_id
            )
        )

        self.db.connection.commit()

    def all(self):

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM scan_history
            ORDER BY id DESC
            """
        )

        columns = [
            column[0]
            for column in cursor.description
        ]

        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def get(self, scan_id):

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM scan_history
            WHERE id = ?
            """,
            (scan_id,)
        )

        row = cursor.fetchone()

        if not row:
            return None

        columns = [
            column[0]
            for column in cursor.description
        ]

        return dict(zip(columns, row))