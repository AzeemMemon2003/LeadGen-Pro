from integration.payload import PayloadBuilder
from integration.webhook import Webhook


class IntegrationManager:

    @staticmethod
    def send(result, proposal_path):

        payload = PayloadBuilder.build(

            result,

            proposal_path

        )

        response = Webhook.send(

            payload

        )

        return payload, response