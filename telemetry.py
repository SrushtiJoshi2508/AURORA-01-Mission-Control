# -------------------- TELEMETRY MODULE --------------------

def show_telemetry(telemetry, log_event):
    print("\n--- SPACECRAFT TELEMETRY ---")

    try:
        telemetry["fuel"] = float(input("Enter Fuel (%): "))
        telemetry["oxygen"] = float(input("Enter Oxygen (%): "))
        telemetry["temperature"] = float(input("Enter Temperature (°C): "))
        telemetry["battery"] = float(input("Enter Battery (%): "))
        telemetry["altitude"] = float(input("Enter Altitude (km): "))

        log_event("Telemetry updated")

        print("\nTelemetry updated successfully.")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


def display_telemetry(telemetry):
    print("\n--- CURRENT TELEMETRY ---")
    print("Fuel       :", telemetry["fuel"], "%")
    print("Oxygen     :", telemetry["oxygen"], "%")
    print("Temperature:", telemetry["temperature"], "°C")
    print("Battery    :", telemetry["battery"], "%")
    print("Altitude   :", telemetry["altitude"], "km")