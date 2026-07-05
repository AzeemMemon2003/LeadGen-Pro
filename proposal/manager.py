from proposal.generator import ProposalGenerator
from proposal.template import ProposalTemplate
from proposal.exporter import ProposalExporter


class ProposalManager:

    @staticmethod
    def generate(result):

        proposal = ProposalGenerator.generate(result)

        content = ProposalTemplate.render(proposal)

        pdf = ProposalExporter.export(

            proposal["company"],

            content

        )

        return pdf