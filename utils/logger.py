from datetime import datetime


class Logger:

    FILE = "logs/leadgen.log"

    @staticmethod
    def info(message):

        Logger.write("INFO", message)

    @staticmethod
    def error(message):

        Logger.write("ERROR", message)

    @staticmethod
    def write(level, message):

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{now}] [{level}] {message}\n"

        print(line.strip())

        with open(Logger.FILE, "a", encoding="utf-8") as file:

            file.write(line)