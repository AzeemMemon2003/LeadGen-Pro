from scraper.registry import EXTRACTORS

from intelligence.qualifier import LeadQualifier
from intelligence.website_intelligence import WebsiteIntelligence
from intelligence.contact import ContactIntelligence

from ai.opportunity import OpportunityEngine


class Container:

    extractors = EXTRACTORS

    qualifier = LeadQualifier()

    website_intelligence = WebsiteIntelligence()

    contact_intelligence = ContactIntelligence()

    opportunity_engine = OpportunityEngine()