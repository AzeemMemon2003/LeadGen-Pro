from database.repository import LeadRepository

repo = LeadRepository()

print("=" * 60)
print("🔍 Lead Search")
print("=" * 60)

keyword = input("\nEnter company or website: ").strip()

results = repo.search(keyword)

if not results:

    print("\n❌ No leads found.")

else:

    print(f"\n✅ Found {len(results)} lead(s)\n")

    for lead in results:

        print("-" * 60)
        print(f"ID       : {lead[0]}")
        print(f"Company  : {lead[1]}")
        print(f"Website  : {lead[2]}")
        print(f"Email    : {lead[3]}")
        print(f"Score    : {lead[4]}")
        print(f"Priority : {lead[5]}")
        print(f"Status   : {lead[6]}")