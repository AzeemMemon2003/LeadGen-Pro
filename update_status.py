from database.repository import LeadRepository

repo = LeadRepository()

print("=" * 60)
print("📝 Update Lead Status")
print("=" * 60)

lead_id = input("\nLead ID: ").strip()

print()

statuses = [
    "Not Contacted",
    "Email Sent",
    "Follow Up",
    "Meeting Booked",
    "Won",
    "Lost"
]

for index, status in enumerate(statuses, start=1):
    print(f"{index}. {status}")

choice = input("\nChoice: ").strip()

try:

    status = statuses[int(choice) - 1]

    repo.update_status(
        int(lead_id),
        status
    )

    print(f"\n✅ Status updated to '{status}'")

except Exception:

    print("\n❌ Invalid selection.")