from database.repository import LeadRepository

repo = LeadRepository()

for lead in repo.all():

    print(lead)