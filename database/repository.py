from datetime import datetime
import json

from database.database import Database
from database.models import LEADS_TABLE


class LeadRepository:

    def __init__(self):

        self.db = Database()

        self.db.execute(LEADS_TABLE)

    def save(self, result):

        qualification = result.get("qualification", {})

        primary_email = ""

        backup_emails = []

        if result["emails"]:

            primary_email = result["emails"][0]

            backup_emails = result["emails"][1:]

        self.db.execute(

            """
            INSERT OR REPLACE INTO leads(

                company,
                website,
                primary_email,
                backup_emails,
                phone,
                address,
                technology,
                score,
                priority,
                status,
                source,
                contact_form,
                whatsapp,
                linkedin,
                created_at,
                updated_at

            )

            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

            """,

            (

                result["company"],

                result["website"],

                primary_email,

                json.dumps(backup_emails),

                result["phones"][0] if result["phones"] else "",

                result["addresses"][0] if result["addresses"] else "",

                json.dumps(result["technology"]),

                qualification.get("score", 0),

                qualification.get("priority", "LOW"),

                "Not Contacted",

                "LeadGen Pro",

                "",

                "",

                result["social"]["linkedin"],

                datetime.now().isoformat(),

                datetime.now().isoformat()

            )

        )

    def all(self):

        return self.db.fetchall(

            """
            SELECT
                id,
                company,
                website,
                primary_email,
                score,
                priority,
                status
            FROM leads
            ORDER BY score DESC
            """
        )

    def search(self, keyword):

        return self.db.fetchall(

            """
            SELECT
                id,
                company,
                website,
                primary_email,
                score,
                priority,
                status
            FROM leads

            WHERE

            company LIKE ?

            OR website LIKE ?

            """,

            (

                f"%{keyword}%",

                f"%{keyword}%"

            )

        )

    def update_status(self, lead_id, status):

        self.db.execute(

            """
            UPDATE leads

            SET

            status=?,
            updated_at=?

            WHERE id=?

            """,

            (

                status,

                datetime.now().isoformat(),

                lead_id

            )

        )