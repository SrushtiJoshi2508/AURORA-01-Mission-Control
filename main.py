# -------------------- AURORA-01 MAIN PROGRAM --------------------

from telemetry import show_telemetry, display_telemetry
from diagnostics import diagnostics
from emergency import emergency_simulation
from mission_decision import mission_decision
from logger import log_event, get_event_log


mission_id = "AURORA-01"
mission_status = "STANDBY"

telemetry = {
    "fuel": 82,
    "oxygen": 94,
    "temperature": 27,
    "battery": 76,
    "altitude": 12500
}


def show_header():
    print("\n======================================")
    print("       AURORA-01 MISSION CONTROL")
    print("======================================")


def start_mission():
    global mission_status

    mission_status = "ACTIVE"
    log_event("Mission started")

    print("\nMission", mission_id, "started successfully.")
    print("Mission Status:", mission_status)


def show_event_log():
    print("\n--- MISSION EVENT LOG ---")

    events = get_event_log()

    if not events:
        print("No events recorded.")
    else:
        for event in events:
            print(event)


def save_mission_data():
    try:
        with open("mission_log.txt", "w") as file:
            file.write("AURORA-01 MISSION DATA\n")
            file.write("======================\n")
            file.write("Mission Status: " + mission_status + "\n\n")

            file.write("Telemetry:\n")
            file.write("Fuel: " + str(telemetry["fuel"]) + "%\n")
            file.write("Oxygen: " + str(telemetry["oxygen"]) + "%\n")
            file.write("Temperature: " + str(telemetry["temperature"]) + "°C\n")
            file.write("Battery: " + str(telemetry["battery"]) + "%\n")
            file.write("Altitude: " + str(telemetry["altitude"]) + " km\n\n")

            file.write("Event Log:\n")

            for event in get_event_log():
                file.write(event + "\n")

        print("\nMission data saved successfully.")

    except Exception as error:
        print("Error saving mission data:", error)


def mission_summary():
    print("\n--- MISSION SUMMARY ---")
    print("Mission ID     :", mission_id)
    print("Mission Status :", mission_status)

    display_telemetry(telemetry)

    print("\nTotal Events:", len(get_event_log()))


def main():

    while True:

        show_header()

        print("\n1. Start Mission")
        print("2. Show Telemetry")
        print("3. System Diagnostics")
        print("4. Mission Decision")
        print("5. Emergency Simulation")
        print("6. Show Event Log")
        print("7. Save Mission Data")
        print("8. Mission Summary")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            start_mission()

        elif choice == "2":
            show_telemetry(telemetry, log_event)

        elif choice == "3":
            diagnostics(telemetry, log_event)

        elif choice == "4":
            mission_decision(telemetry, log_event)

        elif choice == "5":
            emergency_simulation(telemetry, log_event)

        elif choice == "6":
            show_event_log()

        elif choice == "7":
            save_mission_data()

        elif choice == "8":
            mission_summary()

        elif choice == "9":
            print("\nExiting AURORA-01 Mission Control.")
            break

        else:
            print("\nInvalid choice. Please select 1-9.")


if __name__ == "__main__":
    main()