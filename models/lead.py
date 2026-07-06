from dataclasses import dataclass, field


@dataclass
class Lead:

    company: str = ""

    website: str = ""

    title: str = ""

    emails: list = field(default_factory=list)

    phones: list = field(default_factory=list)

    addresses: list = field(default_factory=list)

    technology: list = field(default_factory=list)

    seo: dict = field(default_factory=dict)

    website_intelligence: dict = field(default_factory=dict)

    social: dict = field(default_factory=dict)

    crawl_pages: list = field(default_factory=list)

    qualification: dict = field(default_factory=dict)

    contact: dict = field(default_factory=dict)

    opportunity: dict = field(default_factory=dict)