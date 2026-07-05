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
        website = result.get("website_intelligence", {})
        contact = result.get("contact", {})

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

                website_score,
                website_strengths,
                website_weaknesses,
                website_opportunities,

                created_at,
                updated_at

            )

            VALUES(

                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?,?,?,?,
                ?,?,?

            )

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

                str(contact.get("has_contact_form", False)),
                str(contact.get("has_whatsapp", False)),

                result["social"].get("linkedin", ""),

                website.get("website_score", 0),

                json.dumps(
                    website.get("strengths", []),
                    ensure_ascii=False
                ),

                json.dumps(
                    website.get("weaknesses", []),
                    ensure_ascii=False
                ),

                json.dumps(
                    website.get("sales_opportunities", []),
                    ensure_ascii=False
                ),

                datetime.now().isoformat(),
                datetime.now().isoformat()

            )

        )

    def all(self):

        rows = self.db.fetchall(

            """
            SELECT

                company,
                website,
                primary_email,
                phone,
                technology,
                score,
                priority,
                status,
                website_score,
                contact_form

            FROM leads

            ORDER BY score DESC

            """

        )

        leads = []

        for row in rows:

            technology = []

            try:
                technology = json.loads(row[4]) if row[4] else []
            except:
                pass

            leads.append({

                "company": row[0],
                "website": row[1],
                "primary_email": row[2],
                "phone": row[3],
                "technology": technology,
                "score": row[5],
                "priority": row[6],
                "status": row[7],
                "website_score": row[8] or 0,
                "contact_form": row[9] == "True"

            })

        return leads

    def search(self, keyword):

        return self.db.fetchall(

            """
            SELECT

                id,
                company,
                website,
                primary_email,
                score,
                website_score,
                priority,
                status

            FROM leads

            WHERE

            company LIKE ?

            OR website LIKE ?

            ORDER BY score DESC

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