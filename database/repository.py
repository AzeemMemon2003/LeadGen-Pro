from datetime import datetime
import json

from database.database import Database
from database.models import LEADS_TABLE


class LeadRepository:

    def __init__(self):

        self.db = Database()
        self.db.execute(LEADS_TABLE)

    @staticmethod
    def _loads(value, default=None):

        if default is None:
            default = []

        if not value:
            return default

        try:
            return json.loads(value)
        except Exception:
            return default

    def exists(self, website):

        row = self.db.fetchone(

            """
            SELECT id
            FROM leads
            WHERE website = ?
            LIMIT 1
            """,

            (website,)

        )

        return row is not None

    def save(self, result):

        qualification = result.get("qualification", {})
        website = result.get("website_intelligence", {})
        contact = result.get("contact", {})
        email_verification = result.get("email_verification", {})

        emails = result.get("emails", [])
        phones = result.get("phones", [])
        addresses = result.get("addresses", [])

        primary_email = contact.get("primary_email", "")

        backup_emails = contact.get("backup_emails", [])

        if not primary_email and emails:
            primary_email = emails[0]

            if not backup_emails and len(emails) > 1:
             backup_emails = emails[1:]

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
                email_verified,
                email_confidence,
                email_provider,
                email_role,
                email_disposable,   
                created_at,
                updated_at

            )

            VALUES(

                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?,?,?,?,?,
                ?,?,?,?,?,
                ?,?

            )

            """,

            (

                result.get("company", ""),
                result.get("website", ""),

                primary_email,
                json.dumps(backup_emails),

                phones[0] if phones else "",
                addresses[0] if addresses else "",

                json.dumps(result.get("technology", [])),

                qualification.get("score", 0),
                qualification.get("priority", "LOW"),

                "Not Contacted",

                "LeadGen Pro",

                str(contact.get("has_contact_form", False)),
                str(contact.get("has_whatsapp", False)),

                result.get("social", {}).get("linkedin", ""),

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
                str(email_verification.get("verified", False)),

                email_verification.get("confidence", 0),

                email_verification.get("provider", ""),

                str(email_verification.get("role_account", False)),

                str(email_verification.get("disposable", False)),

                datetime.now().isoformat(),

                datetime.now().isoformat()

            )

        )

    def all(self):

        rows = self.db.fetchall(

            """
            SELECT

                id,
                company,
                website,
                primary_email,
                phone,
                technology,
                score,
                priority,
                status,
                website_score,
                contact_form,
                email_verified,
                email_confidence,
                email_provider,
                email_role,
                email_disposable

            FROM leads

            ORDER BY score DESC

            """

        )

        leads = []

        for row in rows:
        
            leads.append({

            "id": row["id"],
            "company": row["company"],
            "website": row["website"],
            "primary_email": row["primary_email"],
            "phone": row["phone"],
            "technology": self._loads(row["technology"]),
            "score": row["score"],
            "priority": row["priority"],
            "status": row["status"],
            "website_score": row["website_score"] or 0,
            "contact_form": row["contact_form"] == "True",

            "email_verified": row["email_verified"] == "True",
            "email_confidence": row["email_confidence"] or 0,
            "email_provider": row["email_provider"] or "",
            "email_role": row["email_role"] == "True",
            "email_disposable": row["email_disposable"] == "True"

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

                status = ?,
                updated_at = ?

            WHERE id = ?

            """,

            (

                status,
                datetime.now().isoformat(),
                lead_id

            )

        )