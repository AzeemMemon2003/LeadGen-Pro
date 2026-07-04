import json
import os


class ResumeState:

    FILE = "state/progress.json"

    @classmethod
    def save(cls, index):

        os.makedirs("state", exist_ok=True)

        with open(cls.FILE, "w") as f:

            json.dump(
                {
                    "index": index
                },
                f,
                indent=4
            )

    @classmethod
    def load(cls):

        if not os.path.exists(cls.FILE):

            return 0

        try:

            with open(cls.FILE, "r") as f:

                data = json.load(f)

            return data.get("index", 0)

        except:

            return 0

    @classmethod
    def clear(cls):

        if os.path.exists(cls.FILE):

            os.remove(cls.FILE)