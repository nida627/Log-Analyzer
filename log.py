import re
import os
from datetime import datetime

LOG_FILE = "logs.txt"
REPORT_FILE = "report.txt"


def analyze_logs():

    if not os.path.exists(LOG_FILE):
        print("\nLog file not found!")
        return

    pattern = r"(\d{4}-\d{2}-\d{2})\s(\d{2}:\d{2}:\d{2})\s(INFO|WARNING|ERROR)\s(.+)"

    total_logs = 0
    invalid_logs = 0

    info_count = 0
    warning_count = 0
    error_count = 0

    error_messages = []

    print("\nReading Log File...")
    print("Parsing Logs...\n")

    with open(LOG_FILE, "r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            match = re.match(pattern, line)

            if match:

                total_logs += 1

                date = match.group(1)
                time = match.group(2)
                level = match.group(3)
                message = match.group(4)

                if level == "INFO":
                    info_count += 1

                elif level == "WARNING":
                    warning_count += 1

                elif level == "ERROR":
                    error_count += 1
                    error_messages.append(f"{date} {time} - {message}")

            else:

                invalid_logs += 1
                print("Invalid Log :", line)

    generate_report(
        total_logs,
        info_count,
        warning_count,
        error_count,
        invalid_logs,
        error_messages
    )

    print("\n" + "=" * 40)
    print("      ANALYSIS SUMMARY")
    print("=" * 40)

    print(f"Total Logs     : {total_logs}")
    print(f"INFO Logs      : {info_count}")
    print(f"WARNING Logs   : {warning_count}")
    print(f"ERROR Logs     : {error_count}")
    print(f"Invalid Logs   : {invalid_logs}")

    print("\nReport Generated Successfully!")
    print(f"Report Saved As : {REPORT_FILE}")


def generate_report(total, info, warning, error, invalid, errors):

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open(REPORT_FILE, "w") as report:

        report.write("=" * 45 + "\n")
        report.write("          LOG ANALYSIS REPORT\n")
        report.write("=" * 45 + "\n\n")

        report.write(f"Generated On : {current_time}\n\n")

        report.write(f"Total Logs      : {total}\n")
        report.write(f"INFO Logs       : {info}\n")
        report.write(f"WARNING Logs    : {warning}\n")
        report.write(f"ERROR Logs      : {error}\n")
        report.write(f"Invalid Logs    : {invalid}\n")

        report.write("\n" + "=" * 45 + "\n")
        report.write("ERROR DETAILS\n")
        report.write("=" * 45 + "\n")

        if errors:

            for err in errors:
                report.write(err + "\n")

        else:

            report.write("No Errors Found.\n")


def menu():

    while True:

        print("\n" + "=" * 40)
        print("          LOG ANALYZER")
        print("=" * 40)
        print("1. Analyze Log File")
        print("2. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            analyze_logs()

        elif choice == "2":

            print("\nThank You!")
            break

        else:

            print("\nInvalid Choice! Please Try Again.")


menu()