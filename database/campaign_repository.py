from database.database import Database


class CampaignRepository:

    def __init__(self):

        self.db = Database()

    def all(self):

        query = """
        SELECT *
        FROM campaigns
        ORDER BY id DESC
        """

        return self.db.fetchall(query)

    def get(self, campaign_id):

        query = """
        SELECT *
        FROM campaigns
        WHERE id = ?
        """

        return self.db.fetchone(query, (campaign_id,))