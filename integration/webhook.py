import requests

from config.settings import Settings


class Webhook:

    @staticmethod
    def send(payload):

        # Webhook disabled
        if not getattr(Settings, "N8N_WEBHOOK", ""):
            return {
                "success": False,
                "message": "N8N webhook not configured."
            }

        try:

            response = requests.post(

                Settings.N8N_WEBHOOK,

                json=payload,

                timeout=20

            )

            response.raise_for_status()

            return {

                "success": True,

                "status_code": response.status_code,

                "response": response.text

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }