from ranking.email_ranker import EmailRanker

emails = [
    "privacy@company.com",
    "support@company.com",
    "info@company.com",
    "sales@company.com",
    "contact@company.com",
    "hello@company.com",
    "noreply@company.com"
]

result = EmailRanker.rank(emails)

print(result)