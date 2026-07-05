from analytics.metrics import Metrics


class Dashboard:

    @staticmethod
    def show():

        data = Metrics.summary()

        print()
        print("=" * 70)
        print("              🚀 LEADGEN PRO ANALYTICS")
        print("=" * 70)

        print(f"📊 Total Leads           : {data['total']}")
        print(f"⭐ High Priority         : {data['high_priority']}")
        print(f"📧 Leads With Email      : {data['emails']}")
        print(f"📞 Leads With Phone      : {data['phones']}")
        print(f"🌐 Average Website Score : {data['average_score']}")

        print()
        print("=" * 70)
        print("💻 TOP TECHNOLOGIES")
        print("=" * 70)

        if data["technologies"]:

            for tech, count in list(data["technologies"].items())[:10]:

                print(f"{tech:<30} {count}")

        else:

            print("No technologies detected.")

        print("=" * 70)


if __name__ == "__main__":

    Dashboard.show()